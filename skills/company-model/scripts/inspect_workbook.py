"""Read workbook structure and cached values without Excel, recalculation or writes.

Usage: python inspect_workbook.py model.xlsx --output snapshot.json
Inspect every sheet without inferring financial meaning from its name or colours.
This is a structural inspection, not a formula or model-validity certification.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET

N={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
   'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
P='http://schemas.openxmlformats.org/package/2006/relationships'
def tag(name):return '{'+N['s']+'}'+name
def attrs(el):return dict(el.attrib) if el is not None else {}

def inspect(path: Path) -> dict:
 data=path.read_bytes()
 result={'path':str(path.resolve()),'sha256':hashlib.sha256(data).hexdigest(),
         'bytes':len(data),'inspection':'OOXML read only; cached values not recalculated',
         'modified_utc':datetime.fromtimestamp(path.stat().st_mtime,timezone.utc).isoformat()}
 with zipfile.ZipFile(path) as z:
  names=z.namelist();wb=ET.fromstring(z.read('xl/workbook.xml'))
  rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
  targets={x.get('Id'):x.get('Target') for x in rels}
  strings=[]
  if 'xl/sharedStrings.xml' in names:
   ss=ET.fromstring(z.read('xl/sharedStrings.xml'))
   strings=[''.join(si.itertext()) for si in ss]
  styles=ET.fromstring(z.read('xl/styles.xml')) if 'xl/styles.xml' in names else None
  fonts=styles.find('s:fonts',N) if styles is not None else []
  xfs=styles.find('s:cellXfs',N) if styles is not None else []
  fills=styles.find('s:fills',N) if styles is not None else []
  result['features']={
   'charts':sum(bool(re.fullmatch(r'xl/charts/chart\d+\.xml',n)) for n in names),
   'images':sum(n.startswith('xl/media/') for n in names),
   'external_link_parts':sum(bool(re.fullmatch(r'xl/externalLinks/externalLink\d+\.xml',n)) for n in names),
   'vba':any('vbaProject' in n for n in names),
   'legacy_drawing_or_controls':sum('/ctrlProps/' in n or n.endswith('.vml') for n in names)}
  result['calculation_properties']=attrs(wb.find('s:calcPr',N))
  result['defined_names']=[{'name':e.get('name'),'ref':e.text} for e in wb.findall('s:definedNames/s:definedName',N)][:35]
  result['sheets']=[]
  for sh in wb.findall('s:sheets/s:sheet',N):
   target=targets[sh.get('{'+N['r']+'}id')]
   part=target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/'+target)
   xml=z.read(part);tree=ET.fromstring(xml)
   formulas=[];errors=[];headers=[];labels=[];input_samples=[]
   fc=Counter();fillc=Counter();colorc=Counter();formula_count=0;cells=0
   for c in tree.findall('.//s:sheetData/s:row/s:c',N):
    addr=c.get('r','');v=c.find('s:v',N);value=v.text if v is not None else None
    t=c.get('t');f=c.find('s:f',N)
    if t=='s' and value is not None:value=strings[int(value)]
    elif t=='inlineStr':value=''.join(c.find('s:is',N).itertext())
    if f is None and value is None:continue
    cells+=1
    sid=int(c.get('s','0'));xf=xfs[sid] if xfs is not None and sid<len(xfs) else None
    font=fonts[int(xf.get('fontId','0'))] if xf is not None else None
    fname=font.find('s:name',N) if font is not None else None
    color=attrs(font.find('s:color',N)) if font is not None else {}
    colortext=json.dumps(color,sort_keys=True)
    if fname is not None:fc[fname.get('val')]+=1
    colorc[colortext]+=1
    if xf is not None:fillc[xf.get('fillId','0')]+=1
    rownum=int(re.search(r'\d+',addr).group()) if re.search(r'\d+',addr) else 0
    if rownum<=3 and value is not None:headers.append({'cell':addr,'value':value})
    islabel=bool(re.match(r'^[AB]\d+$',addr)) and isinstance(value,str) and t in ['s','inlineStr']
    if islabel:labels.append({'cell':addr,'text':value})
    if f is not None:
     formula_count+=1
     if len(formulas)<12:
      formulas.append({'cell':addr,'formula':f.text,'cached':value})
    if t=='e':errors.append({'cell':addr,'cached_error':value})
    if f is None and t not in ['s','inlineStr','e','b','str'] and value is not None and len(input_samples)<8:
     input_samples.append({'cell':addr,'value':value,'font_color':color})
   views=tree.find('s:sheetViews/s:sheetView',N)
   pane=views.find('s:pane',N) if views is not None else None
   columns=[attrs(c) for c in tree.findall('s:cols/s:col',N)][:12]
   result['sheets'].append({'name':sh.get('name'),'state':sh.get('state','visible'),
    'dimension':attrs(tree.find('s:dimension',N)).get('ref'),'populated_cells':cells,
    'formula_count':formula_count,'cached_error_count':len(errors),'cached_errors':errors[:30],'cached_errors_truncated':len(errors)>30,
    'x14_or_extension':b'2009/9/main' in xml or b'<extLst' in xml or b':extLst' in xml,
    'fonts':dict(fc.most_common(5)),'font_colors':dict(colorc.most_common(7)),
    'fill_ids':dict(fillc.most_common(5)),
    'gridlines':views.get('showGridLines') if views is not None else None,'freeze_pane':attrs(pane),
    'columns':columns,'headers':headers[:60],'row_labels':labels,
    'formula_samples':formulas,'numeric_input_samples':input_samples})
  result['fills']=[ET.tostring(f,encoding='unicode') for f in fills][:16]
 return result

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('workbook',type=Path);parser.add_argument('--output',type=Path)
 args=parser.parse_args();result=inspect(args.workbook)
 text=json.dumps(result,ensure_ascii=False,indent=2)
 if args.output:
  args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text,encoding='utf-8')
 else:print(text)
if __name__=='__main__':main()

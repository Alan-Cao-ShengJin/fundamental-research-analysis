"""Trace selected Excel cells read-only; identify local/cross-sheet precedents.

python trace_model.py book.xlsx --cell "Operating build!F15" --output trace.json
Does not recalculate, refresh sources, execute macros or modify the source.
Unresolved references are explicit; leaf inputs are candidates, not verified facts.
Requires openpyxl. Existing workbook features are never re-exported.
"""
import argparse,hashlib,json,re,warnings
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.formula import Tokenizer
from openpyxl.utils.cell import range_boundaries,get_column_letter


def trace(path, selections, max_depth=8, max_nodes=350, max_range_cells=150):
    path=Path(path);before=hashlib.sha256(path.read_bytes()).hexdigest()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        formulas=load_workbook(path,read_only=False,data_only=False,keep_links=True)
        cached=load_workbook(path,read_only=False,data_only=True,keep_links=True)
    nodes={};unresolved=[]
    def visit(sheet,addr,depth):
        key=sheet+'!'+addr
        if key in nodes:return
        if len(nodes)>=max_nodes:
            unresolved.append({'from':key,'reason':'node limit'});return
        if sheet not in formulas.sheetnames:
            unresolved.append({'from':key,'reason':'unknown sheet'});return
        c=formulas[sheet][addr];value=c.value
        label=[]
        context_columns=sorted(set(range(1,min(4,c.column)))|set(range(max(1,c.column-4),c.column)))
        for ci in context_columns:
            v=formulas[sheet].cell(c.row,ci).value
            if isinstance(v,str) and not v.startswith('='):label.append(v)
        node={'sheet':sheet,'cell':addr,'value':str(value) if not isinstance(value,(str,int,float,bool,type(None))) else value,'cache':cached[sheet][addr].value,'row_context':label,'note':c.comment.text if c.comment else None,'precedents':[],'kind':'formula' if c.data_type=='f' else 'input_candidate','depth':depth}
        nodes[key]=node
        if c.data_type!='f':return
        if not isinstance(value,str):
            unresolved.append({'from':key,'reason':'array/data-table formula object'});return
        try:tokens=Tokenizer(value).items
        except Exception as exc:
            unresolved.append({'from':key,'reason':'unparsed formula: '+str(exc)});return
        for token in tokens:
            if token.type!='OPERAND' or token.subtype!='RANGE':continue
            ref=token.value;target_sheet=sheet
            if '[' in ref or ']' in ref:
                unresolved.append({'from':key,'reference':ref,'reason':'external workbook or structured reference'});continue
            if '!' in ref:
                target_sheet,ref=ref.rsplit('!',1);target_sheet=target_sheet.strip("'").replace("''", "'")
            ref=ref.replace('$','')
            if not re.fullmatch(r'[A-Za-z]+[1-9][0-9]*(?::[A-Za-z]+[1-9][0-9]*)?',ref):
                unresolved.append({'from':key,'reference':token.value,'reason':'name, dynamic or unsupported range; resolve manually'});continue
            left,top,right,bottom=range_boundaries(ref)
            if (right-left+1)*(bottom-top+1)>max_range_cells:
                unresolved.append({'from':key,'reference':token.value,'reason':'range expansion limit'});continue
            for ri in range(top,bottom+1):
                for ci in range(left,right+1):
                    target=f'{get_column_letter(ci)}{ri}'
                    node['precedents'].append({'sheet':target_sheet,'cell':target,'same_sheet':target_sheet==sheet,'row_distance':abs(c.row-ri) if target_sheet==sheet else None})
                    if depth<max_depth:visit(target_sheet,target,depth+1)
                    else:unresolved.append({'from':key,'reference':target_sheet+'!'+target,'reason':'depth limit'})
    try:
        for selection in selections:
            sheet,addr=selection.rsplit('!',1);visit(sheet.strip("'"),addr.replace('$','').upper(),0)
    finally:formulas.close();cached.close()
    after=hashlib.sha256(path.read_bytes()).hexdigest()
    if before!=after:raise RuntimeError('Workbook changed during read; do not trust this snapshot')
    return {'path':str(path.resolve()),'sha256':before,'inspection':'Read only; saved formulas and caches, not recalculated','nodes':nodes,'unresolved':unresolved,'limits':'Local references and row distance describe navigation only. Input candidates may be actuals, estimates, overrides or technical constants. Verify meaning, evidence and forecast purpose manually.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook',type=Path);parser.add_argument('--cell',action='append',required=True)
    parser.add_argument('--depth',type=int,default=8);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=trace(args.workbook,args.cell,max_depth=args.depth)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    print(json.dumps({'nodes':len(result['nodes']),'unresolved':len(result['unresolved']),'source_unchanged':True,'output':str(args.output)}))

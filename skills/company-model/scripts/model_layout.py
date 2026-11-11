"""Reusable worksheet construction primitives; no sector, period or forecast assumptions."""
import model_workbook as mw

class Sheet:
    def __init__(self,name,last='H',notes=None,label_width=46,column_width=11,freeze='D6',tab='BFC7D0'):
        self.name,self.r,self.R=name,6,{}
        self.d={'lastColumn':last,'labelWidth':label_width,'columnWidth':column_width,'freeze':freeze,'tabColor':tab,'sections':[],'cells':{}}
        if notes is not None: self.d['notes']=notes
    def put(self,addr,value,kind='calculation',pct=False,bold=False,fmt=None,**extra):
        if value is None: return
        cell={'value':value,'kind':kind}
        if pct: cell['pct']=True
        if bold: cell['bold']=True
        if fmt: cell['format']=fmt
        cell.update(extra); self.d['cells'][addr]=cell
    def reserve(self,order):
        for key in order.split() if isinstance(order,str) else order: self.R[key]=self.r; self.r+=1
    def section(self,key,title):
        row=self.R[key]; self.put(f'B{row}',title); self.d['sections'].append(row)
    def note(self,row,text):
        if 'notes' not in self.d: raise ValueError('Declare the visible explanation/source column for this sheet')
        self.put(f'{self.d["notes"]}{row}',text)
    def linked_note(self,row,template,inputs,column):
        """Visible live explanation; legacy comment-only notes columns are unsuitable."""
        import re
        from model_text import formula
        if (not isinstance(column,str) or not re.fullmatch('[A-Z]{1,3}',column) or mw.colnum(column)>16384
                or column==self.d.get('notes') or type(row) is not int or not 1<=row<=1048576):
            raise ValueError('Choose an explicit visible column, not the legacy comment-only notes column')
        existing=self.d['cells'].get(f'{column}{row}',{})
        if existing and not existing.get('text') and (not isinstance(existing.get('value'),str) or mw.is_formula(existing['value'])):
            raise ValueError('A linked explanation cannot overwrite an existing input or business formula')
        self.put(f'{column}{row}',formula(template,inputs),text=True,wrap=True)
        self.d.setdefault('widths',{}).setdefault(column,60)
        if mw.colnum(column)>mw.colnum(self.d['lastColumn']): self.d['lastColumn']=column
    def period_sheet(self,forecast_columns,group_columns=(),spacer=None):
        self.d.update(tagColumn='D',tags={},headerRows=[4,5],forecastColumns=list(forecast_columns),
                      groupColumns=[list(g) for g in group_columns],groupRows=[],zoom=85)
        if spacer: self.d.setdefault('widths',{})[spacer]=2
    def group_sections(self):
        notes=self.d.get('notes'); used=sorted({mw.split(a)[1] for a in self.d['cells'] if mw.split(a)[0]!=notes})
        starts=sorted(self.d['sections'])
        for i,start in enumerate(starts):
            end=starts[i+1] if i+1<len(starts) else max(used)+1
            body=[r for r in used if start<r<end]
            if len(body)>=3: self.d.setdefault('groupRows',[]).append([start+1,body[-1]-1])

def period_row(sheet,key,label,unit,values,columns,forecast_columns=(),note=None,pct=False,fmt=None,bold=False,tag=None,tags=None):
    row=sheet.R[key]; sheet.put(f'B{row}',label,bold=bold)
    if unit: sheet.put(f'C{row}',unit)
    if note: sheet.note(row,note)
    if tag and 'tagColumn' in sheet.d: sheet.d.setdefault('tags',{})[str(row)]=tag
    if tag and tags is not None: tags[(sheet.name,row)]=tag
    for column in columns:
        value=values(column,row) if callable(values) else values.get(column)
        if value is None: continue
        kind='calculation' if mw.is_formula(value) else 'input' if column in forecast_columns else 'actual'
        sheet.put(f'{column}{row}',value,kind,pct,bold,fmt)
    return row

def header(sheet,title,units,company='',price_date='',case_text=None,status=None,periods=None,regimes=None):
    sheet.put('B1',(company+' | ' if company else '')+title,bold=True,title=True)
    if case_text is not None: sheet.put('B2',case_text,text=True)
    sheet.put('C2',units+(' | prices as of '+price_date if price_date else ''),align='left')
    if status is not None: sheet.put('B3',status,flag=True,text=True)
    if periods:
        sheet.put('B4','Basis'); sheet.put('B5','Period',bold=True)
        for col,period in periods.items():
            if regimes and col in regimes: sheet.put(f'{col}4',regimes[col])
            sheet.put(f'{col}5',period,bold=True)

def text_sheet(name,heads,rows,widths,intro,write_header):
    sheet=Sheet(name,last=mw.colname(1+len(heads)),notes=None,label_width=widths[0],column_width=16,freeze='A6',tab='BDD7EE')
    sheet.d.update(wrap=True,widths=widths[1],unitColumn=None,fitPages=1)
    write_header(sheet,name,intro,periods=False)
    for i,value in enumerate(heads): sheet.put(f'{mw.colname(2+i)}5',value,bold=True)
    for j,row in enumerate(rows):
        for i,value in enumerate(row): sheet.put(f'{mw.colname(2+i)}{6+j}',value)
    return sheet

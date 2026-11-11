"""Render an investment brief with the shared selective HTML template.
Standard library only. Prose is already edited; this script formats and validates it.
"""
from pathlib import Path
from decimal import Decimal
from urllib.parse import urlsplit
import argparse,html,json,math,re

ASSETS=Path(__file__).resolve().parents[1]/'assets'
COLORS={'Buy':'#166245','Hold':'#9B6F1E','Sell':'#993E42'}
def require(condition,message):
    if not condition:raise ValueError(message)
def text(value,field):
    require(isinstance(value,str) and value.strip(),field+' must be nonempty text')
    return value.strip()
def number(value,field,positive=False):
    require(type(value) in (int,float) and math.isfinite(value),field+' must be a finite number')
    require(not positive or value>0,field+' must be positive')
    return value
def href(value):
    value=text(value,'link target');u=urlsplit(value)
    require(u.scheme.lower() in ('','https','http'),'Only relative links or http(s) URLs are allowed')
    require(not value.startswith('//'),'Protocol-relative links are not allowed')
    return value
def esc(x):return html.escape(str(x),quote=True)
def money(x,currency,places=2):
    prefix={'USD':'$','HKD':'HK$','SGD':'S$','EUR':'€','GBP':'£','JPY':'¥','CNY':'CN¥'}.get(currency,currency+' ')
    return prefix+f'{x:,.{places}f}'
def pct(x):return f'{x:+.1%}'
def validate(payload):
    require(isinstance(payload,dict),'Expected an object')
    require(payload.get('schemaVersion')=='2.0.0','Unsupported payload version')
    m=payload['meta'];d=payload['decision']
    for key in ('issuer','security','currency','asOf'):text(m.get(key),'meta.'+key)
    require(bool(re.fullmatch('[A-Z]{3}',m['currency'])),'Use a three-letter currency')
    p=number(d.get('referencePrice'),'referencePrice',True);t=number(d.get('targetPrice'),'targetPrice',True)
    for key in ('priceObservation','targetDate'):text(d.get(key),key)
    # Decimal boundaries retain Hold at exactly +/-10%, before display rounding.
    pd,td=Decimal(str(p)),Decimal(str(t))
    call='Buy' if td>pd*Decimal('1.10') else 'Sell' if td<pd*Decimal('.90') else 'Hold'
    require(d.get('rating')==call,'Rating conflicts with referencePrice and targetPrice in this payload; write the unrounded model values into brief.json')
    for old in ('dividendPerShare','dividendsToTargetDate'):
        require(old not in d, f'Replace {old} with dividendYield; dividends stay out of the target and rating')
    div=d.get('dividendYield')
    if div is not None:
        number(div,'dividendYield');require(div>=0,'Dividend yield cannot be negative')
    for key in ('bearTarget','bullTarget'):number(d.get(key),key,True)
    km=d.get('keyMetrics',[]);require(isinstance(km,list) and len(km)<=4,'Use at most four key metrics')
    for x in km:text(x,'keyMetrics item')
    require(not km or div is None or any('dividend yield' in x for x in km),'Include the dividend yield in keyMetrics')
    for key in ('bearBasis','targetBasis','bullBasis'):
        if d.get(key) is not None:text(d[key],key)
    require(d['bearTarget']<=t<=d['bullTarget'],'Scenario targets must bracket the primary target')
    text(payload.get('headline'),'headline')
    ss=payload.get('sections');require(isinstance(ss,list) and len(ss)>0,'At least one substantive section required')
    section_ids=[]
    for section in ss:
        ident=text(section.get('id'),'section.id');text(section.get('title'),'section.title')
        require(bool(re.fullmatch('[a-z][a-z0-9-]*',ident)),'Use a safe section ID')
        section_ids.append(ident)
    require(len(set(section_ids))==len(section_ids),'Duplicate section IDs')
    sources=payload.get('sources',[]);require(isinstance(sources,list) and len(sources)<=6,'Use at most six compact source entries')
    ids=[]
    for s in sources:
        ids.append(text(s.get('id'),'source.id'));text(s.get('label'),'source.label');href(s.get('href'))
    require(len(set(ids))==len(ids),'Duplicate source IDs')
    for s in ss:
        require(isinstance(s.get('paragraphs'),list) and len(s['paragraphs'])>0,s['title']+' needs substantive prose')
        for paragraph in s['paragraphs']:text(paragraph,s['title'])
        require(isinstance(s.get('sourceIds',[]),list) and set(s.get('sourceIds',[]))<=set(ids),'Unknown source reference')
    f=payload.get('financials')
    if f is not None:
        require(f.get('sectionId') in section_ids,'Financial table needs a selected sectionId')
        text(f.get('caption'),'financial caption')
        require(isinstance(f.get('columns'),list) and 2<=len(f['columns'])<=4,'Financial table needs two to four column headings')
        require(isinstance(f.get('rows'),list) and 1<=len(f['rows'])<=4,'Financial table needs one to four material rows')
        for x in f['columns']:text(x,'financial column heading')
        for row in f['rows']:
            require(len(row)==len(f['columns']),'Financial table width mismatch')
            for x in row:text(x,'financial cell')
    require(isinstance(payload.get('links',[]),list) and len(payload.get('links',[]))<=4,'Too many support links')
    for x in payload.get('links',[]):text(x.get('label'),'link label');href(x.get('href'))
    return {'rating':call,'priceReturn':t/p-1,'dividendYield':div,
            'bearReturn':d['bearTarget']/p-1,'bullReturn':d['bullTarget']/p-1,
            'sectionCount':len(ss),'wordCount':sum(len(re.findall(r"\b[\w']+\b",p)) for s in ss for p in s['paragraphs'])}

def render(payload):
    result=validate(payload);m=payload['meta'];d=payload['decision'];currency=m['currency']
    index={x['id']:i+1 for i,x in enumerate(payload.get('sources',[]))}
    financials=payload.get('financials');table=''
    if financials is not None:
        table='<table><caption>'+esc(financials['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in financials['columns'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+esc(x)+('</th>' if i==0 else '</td>') for i,x in enumerate(row))+'</tr>' for row in financials['rows'])+'</tbody></table>'
    cases=[('Bear',d['bearTarget'],result['bearReturn'],'bear',d.get('bearBasis')),('Base',d['targetPrice'],result['priceReturn'],'base',d.get('targetBasis')),('Bull',d['bullTarget'],result['bullReturn'],'bull',d.get('bullBasis'))]
    scenarios=''.join(f'<div class="scenario {kind}"><span class="case-name">{name}</span><strong>{money(price,currency)}</strong><span class="case-return">{pct(ret)}</span>'+(f'<span class="case-basis">{esc(basis)}</span>' if basis else '')+'</div>' for name,price,ret,kind,basis in cases)
    def section(s):
        citations=''.join(f'<a href="#source-{esc(k)}">[{index[k]}]</a>' for k in s.get('sourceIds',[]))
        paragraphs=''.join('<p>'+esc(p)+(f'<sup>{citations}</sup>' if n==len(s['paragraphs'])-1 and citations else '')+'</p>' for n,p in enumerate(s['paragraphs']))
        extra=table if financials and s['id']==financials['sectionId'] else ''
        return f'<section class="brief-section" data-section="{esc(s["id"])}"><h2>{esc(s["title"])}</h2>{paragraphs}{extra}</section>'
    sources=('Sources: '+''.join(f'<a id="source-{esc(s["id"])}"'+(f' href="{esc(s["href"])}"' if urlsplit(s['href']).scheme else '')+f'>[{i+1}] {esc(s["label"])}</a>' for i,s in enumerate(payload['sources']))) if payload.get('sources') else ''
    links=''.join(f'<a href="{esc(s["href"])}">{esc(s["label"])}</a>' if urlsplit(s['href']).scheme else f'<span>{esc(s["label"])}: {esc(s["href"])}</span>' for s in payload.get('links',[]))
    identity=f'{m["security"]} / {currency}'
    metrics=[('Reference price',money(d['referencePrice'],currency),''),('Price target',money(d['targetPrice'],currency),''),('Price return',pct(result['priceReturn']),'return-value')]
    metrics_html=''.join(f'<div class="metric"><small>{esc(label)}</small><strong class="{cls}">{esc(value)}</strong></div>' for label,value,cls in metrics)
    payoff=f'Price at {esc(d["priceObservation"])}; 12-month target'
    metrics_line=d.get('keyMetrics') or ([f'{result["dividendYield"]*100:.1f}% dividend yield'] if result['dividendYield'] else [])
    for x in metrics_line:payoff+='; '+esc(x)
    payoff+='.'
    substitutions={'TITLE':esc(m['issuer']+' | investment brief'),'ISSUER':esc(m['issuer']),'IDENTITY':esc(identity),'DATE':esc(m['asOf']),'HEADLINE':esc(payload['headline']),'RATING':esc(d['rating']+' | Price return '+pct(result['priceReturn'])),'METRICS':metrics_html,'PAYOFF':payoff,'SECTIONS':''.join(section(s) for s in payload['sections']),'SCENARIOS':scenarios,'SOURCES':sources,'LINKS':links,'RATING_COLOR':COLORS[d['rating']],'RETURN_COLOR':COLORS['Sell'] if result['priceReturn']<0 else COLORS['Buy'] if result['priceReturn']>0 else '#667381'}
    template=(ASSETS/'one-page-brief.template.html').read_text(encoding='utf-8')
    for key,value in substitutions.items():template=template.replace('@@'+key+'@@',value)
    require(not re.search(r'@@[A-Z_]+@@',template),'Unresolved template token')
    return template,result

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--input',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--check',type=Path)
    args=ap.parse_args();payload=json.loads(args.input.read_text(encoding='utf-8'));document,report=render(payload)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(document,encoding='utf-8')
    if args.check:args.check.parent.mkdir(parents=True,exist_ok=True);args.check.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,TypeError) as exc:raise SystemExit(str(exc))

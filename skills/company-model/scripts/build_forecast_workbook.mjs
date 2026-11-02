// Generic authoring adapter for forecast_blocks.py output. No issuer logic.
// node build_forecast_workbook.mjs compiled.json output.xlsx [review-directory]
import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const [input, output, previewDir] = process.argv.slice(2);
if (!input || !output) throw new Error('Pass compiled JSON and a new XLSX path');
try { await fs.access(output); throw new Error('Destination exists; use a new path to preserve prior work'); }
catch (error) { if (error.code !== 'ENOENT') throw error; }
const spec = JSON.parse(await fs.readFile(input, 'utf8'));
const theme=spec.theme;
if(!theme?.colors || !theme?.layout || !theme?.font)throw new Error('Compile with the current forecast_blocks.py to include the model theme');
const {colors,layout}=theme;
if (spec.rows.some(r => r.cells.some(c => c.expected === null))) {
  throw new Error('Incomplete build: resolve missing inputs or undefined arithmetic before delivering a calculated workbook');
}
const wb = Workbook.create();
const ws = wb.worksheets.add('Operating build');
ws.showGridLines = layout.gridlines;
const lastRow = Math.max(...spec.rows.map(r => r.row));
const letter = n => { let s=''; while(n) {n--; s=String.fromCharCode(65+n%26)+s; n=Math.floor(n/26);} return s; };
const lastPeriod = 3 + spec.periods.length;
const noteCol = letter(lastPeriod + 2);
const full = ws.getRange(`A1:${noteCol}${lastRow}`);
full.format.font = { ...theme.font, color:colors.calculation };
full.format.rowHeight = layout.row_height;
full.format.verticalAlignment = 'center';
full.format.horizontalAlignment = layout.alignment;
ws.getRange(`A1:A${lastRow}`).format.columnWidth = 3;
ws.getRange(`B1:B${lastRow}`).format.columnWidth = layout.label_width;
ws.getRange(`C1:C${lastRow}`).format.columnWidth = layout.unit_width;
ws.getRange(`D1:${letter(lastPeriod)}${lastRow}`).format.columnWidth = layout.period_width;
ws.getRange(`${letter(lastPeriod+1)}1:${letter(lastPeriod+1)}${lastRow}`).format.columnWidth = 3;
ws.getRange(`${noteCol}1:${noteCol}${lastRow}`).format.columnWidth = layout.explanation_width;
ws.getRange(`${noteCol}1:${noteCol}${lastRow}`).format.horizontalAlignment=layout.explanation_alignment;
const put = (a,v) => ws.getRange(a).values = [[v]];
put('B2',spec.title);
ws.getRange('B2').format.font = { name:theme.font.name, size:17, bold:true, color:colors.calculation };
ws.getRange('B2').format.horizontalAlignment='left';
put('B4',spec.synthetic ? 'Synthetic example; no company forecasts' : 'Forecast build');
put('B5','Black: calculations. Dark blue: actual inputs. Purple + nude: forecast assumptions. Italic grey: actual/calculated %. Bold: totals.');
ws.getRange('B4:B5').format.horizontalAlignment='left';
ws.getRange('B5').format.font = { name:theme.font.name,size:9,color:colors.explanation };
put('B7','Metric'); put('C7','Unit');
for (let i=0;i<spec.periods.length;i++) put(`${letter(4+i)}7`,spec.periods[i].label);
put(`${noteCol}7`,'Basis and uncertainty beside the assumption');
ws.getRange(`B7:${letter(lastPeriod)}7`).format.fill = colors.section_fill;
ws.getRange(`B7:${noteCol}7`).format.font.bold = true;
ws.getRange(`B7:${letter(lastPeriod)}7`).format.borders={bottom:{style:layout.border_style,color:colors.border}};
function basisText(r) {
  const inputs=r.cells.filter(c=>c.input || (r.assumption && spec.periods.find(p=>p.id===c.period).kind==='forecast'));
  const parts=[];
  for(const [field,label] of [['kind','Basis'],['source','Source'],['source_date','As of'],['rationale','Reason'],['uncertainty','Uncertainty']]) {
    const grouped=new Map();
    for(const c of inputs)if(c.basis[field]) {
      const value=c.basis[field];if(!grouped.has(value))grouped.set(value,[]);grouped.get(value).push(c.period);
    }
    for(const [text,periods] of grouped)parts.push(`${label}${periods.length===inputs.length?'':` (${periods.join('/')})`}: ${text}`);
  }
  return parts.join('. ');
}
for (const s of spec.sections) {
  put(`B${s.row}`,s.title);
  ws.getRange(`B${s.row}:${letter(lastPeriod)}${s.row}`).format.fill = colors.section_fill;
  ws.getRange(`B${s.row}:${letter(lastPeriod)}${s.row}`).format.font.bold = true;
  const next=spec.sections.find(section=>section.row>s.row)?.row ?? lastRow+3;
  const end=Math.min(lastRow,next-3);
  ws.getRange(`B${s.row}:${letter(lastPeriod)}${end}`).format.borders={preset:'outside',style:layout.border_style,color:colors.border};
  ws.getRange(`B${s.row}:${letter(lastPeriod)}${s.row}`).format.borders={bottom:{style:layout.border_style,color:colors.border}};
}
for (const r of spec.rows) {
  put(`B${r.row}`,r.label); put(`C${r.row}`,r.unit);
  if(r.format==='percent') {
    ws.getRange(`B${r.row}:${letter(lastPeriod)}${r.row}`).format.font.italic=true;
    ws.getRange(`B${r.row}:C${r.row}`).format.font.color=colors.percentage;
  }
  for (const c of r.cells) {
    const cell=ws.getRange(c.address);
    if (c.formula) cell.formulas = [[c.formula]]; else cell.values = [[c.value]];
    cell.setNumberFormat(r.format==='percent'?'0.0%;(0.0%);"-"':'#,##0.0;(#,##0.0);"-"');
    const isForecast=spec.periods.find(p=>p.id===c.period).kind==='forecast';
    if(c.input || (r.assumption && isForecast)) {
      cell.format.font.color=isForecast?colors.forecast_input:colors.actual_input;
      if(isForecast)cell.format.fill=colors.forecast_fill;
    } else cell.format.font.color=colors.calculation;
    if(r.format==='percent' && !(isForecast && (c.input || r.assumption)))cell.format.font.color=colors.percentage;
  }
  const note=basisText(r);
  if(note) {
    put(`${noteCol}${r.row}`,note);
    ws.getRange(`${noteCol}${r.row}`).format.wrapText=true;
    ws.getRange(`${noteCol}${r.row}`).format.font.color=colors.explanation;
    const lines=note.split('\n').reduce((n,line)=>n+Math.max(1,Math.ceil(line.length/(layout.explanation_width*1.15))),0);
    ws.getRange(`B${r.row}:${noteCol}${r.row}`).format.rowHeight=Math.max(layout.row_height,lines*13+4);
  }
  if(r.role==='output'||r.subtotal) {
    ws.getRange(`B${r.row}:${letter(lastPeriod)}${r.row}`).format.font.bold=true;
    ws.getRange(`B${r.row}:${letter(lastPeriod)}${r.row}`).format.borders={top:{style:layout.border_style,color:colors.border}};
  }
}
ws.freezePanes.freezeRows(7);
ws.freezePanes.freezeColumns(3);
wb.recalculate();
function reconcileCells() {
  const mismatches=[];
  for(const r of spec.rows) for(const c of r.cells) {
    const actual=ws.getRange(c.address).values[0][0];
    if(typeof actual!=='number'||Math.abs(actual-c.expected)>1e-8*Math.max(1,Math.abs(c.expected))) mismatches.push({cell:c.address,expected:c.expected,actual});
  }
  if(mismatches.length)throw new Error('Calculation differs from independent compiler: '+JSON.stringify(mismatches.slice(0,8)));
}
reconcileCells();
// Exercise a live input change, verify every result, then restore it before export.
const inputRow=spec.rows.find(r=>r.role==='foundation'&&r.cells.some(c=>spec.periods.find(p=>p.id===c.period).kind==='forecast'));
const inputCell=inputRow?.cells.find(c=>spec.periods.find(p=>p.id===c.period).kind==='forecast');
let inputTest=null;
if(inputCell) {
  const previous=ws.getRange(inputCell.address).values[0][0];
  ws.getRange(inputCell.address).values=[[previous*1.1]];
  wb.recalculate();
  const changed=spec.rows.filter(r=>r.role==='output').map(r=>{
    const c=r.cells.find(c=>c.period===inputCell.period);
    return {node:r.id,before:c.expected,after:ws.getRange(c.address).values[0][0]};
  });
  ws.getRange(inputCell.address).values=[[previous]]; wb.recalculate();
  if(!changed.some(r=>Math.abs(r.after-r.before)>1e-8))throw new Error('Representative input change did not reach selected outputs');
  inputTest={cell:inputCell.address,changed,restored:true};
}
reconcileCells();
await fs.mkdir(path.dirname(path.resolve(output)),{recursive:true});
if(previewDir) {
  await fs.mkdir(previewDir,{recursive:true});
  // A static review snapshot avoids a native image-renderer dependency in the CLI.
  // The live, editable calculation model is the exported workbook.
  const escape = v => String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const parts=[];
  for(let ri=8;ri<=lastRow;ri++) {
    const section=spec.sections.find(s=>s.row===ri);
    if(section)parts.push(`<tr class="section"><th colspan="${2+spec.periods.length}">${escape(section.title)}</th><td class="notes"></td></tr>`);
    const r=spec.rows.find(r=>r.row===ri);if(!r)continue;
    const cells=r.cells.map(c=>{
      const forecast=spec.periods.find(p=>p.id===c.period).kind==='forecast';
      const style=(c.input||(r.assumption&&forecast))?(forecast?'forecast':'actual'):'calculation';
      return `<td class="${style}${r.format==='percent'?' percentage':''}">${escape(r.format==='percent'?(c.expected*100).toFixed(1)+'%':c.expected.toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1}))}</td>`;
    }).join('');
    const labelClass=r.format==='percent'?' class="percentage"':'';
    parts.push(`<tr class="${r.role==='output'||r.subtotal?'total':''}"><td${labelClass}>${escape(r.label)}</td><td${labelClass}>${escape(r.unit)}</td>${cells}<td class="notes">${escape(basisText(r))}</td></tr>`);
  }
  const html=`<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(spec.title)}</title><style>body{font:14px/1.4 Arial;color:${colors.calculation};margin:24px}table{border-collapse:collapse;width:100%}th,td{padding:6px 9px;text-align:right;border-bottom:1px solid #e3e3e3}thead,.section{background:${colors.section_fill}}.section th{border:1px solid ${colors.border}}tbody td:first-child{min-width:160px}.calculation{color:${colors.calculation}}.actual{color:${colors.actual_input}}.forecast{color:${colors.forecast_input};background:${colors.forecast_fill}}.total td:not(.notes){font-weight:bold;border-top:1px solid ${colors.border}}.notes{font-weight:normal;text-align:left;min-width:420px;max-width:650px;font-size:12px;color:${colors.explanation}}</style><h1>${escape(spec.title)}</h1><p>Static review snapshot. Change assumptions in the editable Excel workbook.</p><div style="overflow:auto"><table><thead><tr><th>Metric</th><th>Unit</th>${spec.periods.map(p=>`<th>${escape(p.label)}</th>`).join('')}<th>Basis and uncertainty</th></tr></thead><tbody>${parts.join('')}</tbody></table></div></html>`;
  const percentageCss=`.percentage{font-style:italic;color:${colors.percentage}}.forecast.percentage{color:${colors.forecast_input};background:${colors.forecast_fill}}`;
  await fs.writeFile(path.join(previewDir,'forecast-block.html'),html.replace('</style>',percentageCss+'</style>'));
}
const file=await SpreadsheetFile.exportXlsx(wb); await file.save(output);
await fs.writeFile(output+'.checks.json',JSON.stringify({engine:'artifact-tool',all_cells_reconciled:true,inputTest,source_compilation:input,limits:'Synthetic/example calculation and adapter checks; no native Excel session, source verification or investment validation.'},null,2));
console.log(JSON.stringify({output,rows:spec.rows.length,cellsVerified:spec.rows.reduce((n,r)=>n+r.cells.length,0),inputTest}));

// Check print geometry and actual PDF pagination. Never scale, truncate or clip to fit.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
const args=process.argv.slice(2),options={};
for(let i=0;i<args.length;i+=2){if(!args[i]?.startsWith('--')||!args[i+1])throw Error('Use --input <payload.json> --html <file> --pdf <file> --check <file> [--runtime-modules <node_modules>] [--browser-path <executable>]');options[args[i].slice(2)]=args[i+1];}
if(!options.input||!options.html||!options.pdf||!options.check)throw Error('input, html, pdf and check paths are required');
for(const key of Object.keys(options))if(!['input','html','pdf','check','runtime-modules','browser-path','preview'].includes(key))throw Error('Unknown option: '+key);
const require=createRequire(import.meta.url);
const inputBytes=await fs.readFile(options.input),payload=JSON.parse(inputBytes),expected=payload.sections;
if(payload.schemaVersion!=='2.0.0'||!Array.isArray(expected)||!expected.length)throw Error('Use a validated version-2 brief payload');
const load=async name=>{const loaded=await import(pathToFileURL(require.resolve(name,options['runtime-modules']?{paths:[path.dirname(path.resolve(options['runtime-modules']))]}:undefined)).href);return loaded.default??loaded;};
let chromium,PDFDocument;
try { ({chromium}=await load('playwright')); ({PDFDocument}=await load('pdf-lib')); }
catch { throw Error('Optional browser geometry check needs playwright and pdf-lib. Supply an existing --runtime-modules directory, or install those optional dependencies in the host. The production package path uses Chrome/PyMuPDF and still requires actual PDF visual review; no geometry pass has occurred.'); }
const browser=await chromium.launch({headless:true,...(options['browser-path']?{executablePath:options['browser-path']}:{})});
const report={input:path.resolve(options.input),inputSHA256:createHash('sha256').update(inputBytes).digest('hex'),html:path.resolve(options.html),pdf:path.resolve(options.pdf),htmlSHA256:createHash('sha256').update(await fs.readFile(options.html)).digest('hex'),checks:[],pageCount:null,passed:false};
try{
 const page=await browser.newPage({viewport:{width:794,height:1123},deviceScaleFactor:1});const jsErrors=[];page.on('pageerror',e=>jsErrors.push(e.message));
 await page.goto(pathToFileURL(path.resolve(options.html)).href);await page.evaluate(()=>document.fonts.ready);await page.emulateMedia({media:'print'});
 const geom=await page.evaluate(()=>{
  const content=document.querySelector('.brief-content'),sections=[...document.querySelectorAll('.brief-section')],rect=content.getBoundingClientRect();
  const tableFonts=[...content.querySelectorAll('td,th')].map(x=>parseFloat(getComputedStyle(x).fontSize));
  const nodes=[...content.querySelectorAll('p,table,h1,h2,.metric,.scenarios,.identity,.edition,.footer')];
   return {width:rect.width,height:rect.height,maxHeight:269*96/25.4,sectionIds:sections.map(x=>x.dataset.section),sectionTitles:sections.map(x=>{const h=x.querySelector('h2').cloneNode(true);h.querySelector('.number')?.remove();return h.textContent.trim()}),sectionCount:sections.length,headline:content.querySelector('.headline').textContent.trim(),paragraphs:sections.flatMap(x=>[...x.querySelectorAll('p')].map(p=>{const c=p.cloneNode(true);c.querySelectorAll('sup').forEach(s=>s.remove());return c.textContent.trim()})),tableRows:[...content.querySelectorAll('table tr')].map(r=>[...r.children].map(c=>c.textContent.trim())),
   minBodyFont:Math.min(...[...content.querySelectorAll('.brief-section p:not(.payoff)')].map(x=>parseFloat(getComputedStyle(x).fontSize))),
   minTableFont:tableFonts.length?Math.min(...tableFonts):null,
   clipped:nodes.filter(x=>{const s=getComputedStyle(x);return ['hidden','clip'].includes(s.overflowY)||['hidden','clip'].includes(s.overflowX)||s.display==='none'||s.visibility==='hidden'}).map(x=>x.tagName),
   escaped:nodes.filter(x=>{const r=x.getBoundingClientRect();return r.right>rect.right+1||r.left<rect.left-1||r.bottom>rect.bottom+1}).map(x=>x.tagName),
   brokenImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src)};
 });report.geometry=geom;
 if(options.preview){await fs.mkdir(path.dirname(path.resolve(options.preview)),{recursive:true});await page.locator('.brief-page').screenshot({path:path.resolve(options.preview)});}
 report.checks.push({name:'Selected content and reading order preserved',passed:geom.sectionCount===expected.length&&JSON.stringify(geom.sectionIds)===JSON.stringify(expected.map(x=>x.id))&&JSON.stringify(geom.sectionTitles)===JSON.stringify(expected.map(x=>x.title))&&geom.headline===payload.headline&&JSON.stringify(geom.paragraphs)===JSON.stringify(expected.flatMap(s=>s.paragraphs))&&JSON.stringify(geom.tableRows)===JSON.stringify(payload.financials?[payload.financials.columns,...payload.financials.rows]:[])},{name:'A4 printable height',passed:geom.height<=geom.maxHeight+1},{name:'Readable body and table fonts',passed:geom.minBodyFont>=10.5*96/72&&(geom.minTableFont===null||geom.minTableFont>=9*96/72)},{name:'No hidden or clipped content',passed:geom.clipped.length===0&&geom.escaped.length===0},{name:'No script/image errors',passed:jsErrors.length===0&&geom.brokenImages.length===0});
 if(report.checks.some(x=>!x.passed))throw Error('Brief fails geometry/readability checks. Edit prose or use the shared layout; do not shrink or hide it.');
 const bytes=await page.pdf({format:'A4',preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false,scale:1});const pdf=await PDFDocument.load(bytes);report.pageCount=pdf.getPageCount();report.checks.push({name:'Actual exported PDF has exactly one page',passed:report.pageCount===1});
 if(report.pageCount!==1)throw Error('PDF is not one page. Shorten content; no cropped/first-page-only export is permitted.');
 const size=pdf.getPage(0).getSize();report.pdfSizePoints=size;if(Math.abs(size.width-595.28)>2||Math.abs(size.height-841.89)>2)throw Error('Exported page is not A4 portrait');
 await page.emulateMedia({media:'screen'});await page.setViewportSize({width:390,height:844});report.mobile=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
 if(report.mobile.scrollWidth>report.mobile.width+1)throw Error('Mobile page overflows horizontally');
 await fs.mkdir(path.dirname(path.resolve(options.pdf)),{recursive:true});await fs.writeFile(options.pdf,bytes);report.pdfSHA256=createHash('sha256').update(bytes).digest('hex');report.passed=true;
 console.log(JSON.stringify(report,null,2));
}catch(e){report.error=e.message;process.exitCode=1;console.error(e.message);}
finally{await browser.close();await fs.mkdir(path.dirname(path.resolve(options.check)),{recursive:true});await fs.writeFile(options.check,JSON.stringify(report,null,2)+'\n');}

import re
#!/usr/bin/env python3
"""Genera la web estática Cuentalia. Ejecuta: python3 build.py  ->  carpeta ../site"""
import os, shutil, datetime

# ============ CONFIGURACIÓN (lo único que tienes que tocar) ============
SITE_NAME   = "Cuentalia"
SITE_URL    = "https://cuentalia.pages.dev"   # cámbialo por tu dirección final (sin barra al final)
ADSENSE_ID  = ""                          # ej. "ca-pub-1234567890123456" cuando te aprueben AdSense
CONTACT     = "albertomartina30@gmail.com"
# Enlaces de afiliado por herramienta: slug -> [(texto, url), ...]  (déjalo vacío al principio)
AFFILIATES = {
    # "hipoteca": [("Compara hipotecas gratis", "https://tu-enlace-afiliado")],
}
# =======================================================================

OUT = os.environ.get("OUT_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
TODAY = datetime.date.today().isoformat()

CSS = """
:root{--bg:#f4f6fc;--card:#fff;--ink:#162036;--mut:#5b6580;--au:#3b5bfd;--au2:#8a4dff;--acc:var(--au);--acc2:color-mix(in srgb,var(--acc) 11%,var(--card));--bd:#e1e6f2;--g1:var(--au);--g2:var(--au2);--ok:#12b886;--sh:0 6px 24px rgba(40,60,140,.08)}
[data-t=dark]{--bg:#0e1424;--card:#171f35;--ink:#e8ecf7;--mut:#9aa5c4;--acc:color-mix(in srgb,var(--au) 62%,#fff);--acc2:color-mix(in srgb,var(--au) 22%,var(--card));--bd:#2a3556;--sh:0 6px 24px rgba(0,0,0,.35)}
*{box-sizing:border-box}html{scroll-behavior:smooth;font-size:var(--fs,100%)}body{margin:0;font:1rem/1.65 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--ink);transition:background .25s,color .25s}
a{color:var(--acc)}header{background:var(--card);border-bottom:1px solid var(--bd);position:sticky;top:0;z-index:5;backdrop-filter:blur(8px)}
.w{max-width:960px;margin:0 auto;padding:0 18px}
.top{display:flex;align-items:center;justify-content:space-between;height:62px;gap:10px}
.top nav{display:flex;align-items:center;gap:6px}.top nav a{text-decoration:none;color:var(--mut);font-size:0.875rem;padding:6px 10px;border-radius:8px}.top nav a:hover{background:var(--acc2);color:var(--acc)}
.logo{font-weight:800;font-size:1.3125rem;text-decoration:none;color:var(--ink);letter-spacing:-.3px}.logo span{background:linear-gradient(90deg,var(--g1),var(--g2));-webkit-background-clip:text;background-clip:text;color:transparent}
#th{margin:0;background:var(--acc2);color:var(--ink);padding:7px 11px;border-radius:10px;font-size:1rem;line-height:1}
main{padding:22px 0 56px}h1{font-size:1.875rem;line-height:1.2;margin:8px 0 6px;letter-spacing:-.5px}h2{font-size:1.3125rem;margin:32px 0 10px}
.lead{color:var(--mut);margin:0 0 18px}
.bc{font-size:.85rem;color:var(--mut);margin-bottom:8px}.bc a{text-decoration:none}
details{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:12px 16px;margin:8px 0;transition:box-shadow .2s}details[open]{box-shadow:var(--sh)}summary{cursor:pointer;font-weight:600}
.card{background:var(--card);border:1px solid var(--bd);border-radius:18px;padding:22px;margin:16px 0;box-shadow:var(--sh)}
label{display:block;font-weight:600;font-size:0.875rem;margin:12px 0 5px}
input,select,textarea{width:100%;padding:12px 13px;border:1px solid var(--bd);border-radius:12px;font:inherit;background:var(--card);color:var(--ink);transition:border-color .15s,box-shadow .15s}
input:focus,select:focus,textarea:focus{outline:0;border-color:var(--acc);box-shadow:0 0 0 4px color-mix(in srgb,var(--acc) 20%,transparent)}
textarea{min-height:160px;resize:vertical}
.row{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:560px){.row{grid-template-columns:1fr}}
button{background:linear-gradient(90deg,var(--g1),var(--g2));color:#fff;border:0;border-radius:12px;padding:12px 20px;font:inherit;font-weight:700;cursor:pointer;margin-top:14px;transition:transform .1s,filter .15s}
button:hover{filter:brightness(1.08)}button:active{transform:scale(.97)}
button.sec{background:var(--acc2);color:var(--acc)}
.res{margin-top:18px;display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;animation:up .35s ease}
.res div{background:var(--acc2);border-radius:12px;padding:13px 14px}.res b{display:block;font-size:1.4375rem;letter-spacing:-.3px;color:var(--ink)}.res small{color:var(--mut)}
@keyframes up{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.acts{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 4px}.acts button{margin:0;padding:8px 13px;font-size:0.875rem;background:var(--card);color:var(--ink);border:1px solid var(--bd)}.acts button:hover{border-color:var(--acc);color:var(--acc);filter:none}.acts button.on{background:#fff4d6;border-color:#f5b301;color:#8a5a00}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}
.tool{display:block;background:var(--card);border:1px solid var(--bd);border-radius:16px;padding:16px 16px 14px;text-decoration:none;color:var(--ink);transition:transform .15s,box-shadow .15s,border-color .15s}
.tool:hover{border-color:var(--acc);transform:translateY(-3px);box-shadow:var(--sh)}.tool b{display:block;margin:2px 0 3px}.tool span{color:var(--mut);font-size:0.875rem;display:block}.tool i{font-style:normal;font-size:1.375rem}
.hero{background:linear-gradient(135deg,var(--g1),var(--g2));color:#fff;border-radius:24px;padding:34px 26px;margin:6px 0 20px;box-shadow:var(--sh)}
.hero h1{color:#fff;font-size:2.125rem;margin:0 0 8px}.hero p{margin:0 0 16px;opacity:.92}
.hero input{border:0;font-size:1.0625rem;padding:15px 16px;box-shadow:0 8px 24px rgba(0,0,0,.18)}
.stats{display:flex;gap:18px;flex-wrap:wrap;margin-top:14px;font-size:0.875rem;opacity:.95}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0}.chip{margin:0;padding:8px 14px;font-size:0.875rem;background:var(--card);color:var(--ink);border:1px solid var(--bd);border-radius:999px}.chip.on{background:var(--acc);color:#fff;border-color:var(--acc)}
.day{display:flex;align-items:center;gap:14px;background:var(--card);border:1px dashed var(--acc);border-radius:16px;padding:14px 18px;margin:0 0 6px;text-decoration:none;color:var(--ink)}.day small{color:var(--acc);font-weight:700;text-transform:uppercase;letter-spacing:.5px}.day b{display:block}
.ad{min-height:100px;margin:16px 0;text-align:center}
.aff{border:1px dashed var(--acc);border-radius:14px;padding:12px 16px;background:var(--card)}
.none{display:none;text-align:center;color:var(--mut);padding:20px}
footer{border-top:1px solid var(--bd);background:var(--card);padding:22px 0;color:var(--mut);font-size:0.875rem}
footer a{margin-right:14px}
#toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(20px);background:#162036;color:#fff;padding:10px 18px;border-radius:999px;font-size:0.875rem;opacity:0;pointer-events:none;transition:.25s;z-index:20}#toast.s{opacity:1;transform:translateX(-50%)}
#cb{position:fixed;left:0;right:0;bottom:0;background:#162036;color:#fff;padding:14px 16px;display:none;z-index:9}
#cb .w{display:flex;gap:12px;align-items:center;flex-wrap:wrap}#cb p{margin:0;flex:1;min-width:220px;font-size:0.875rem}
#cb button{margin:0;padding:9px 14px}
@media(max-width:560px){h1{font-size:1.5625rem}.hero{padding:24px 18px}.hero h1{font-size:1.625rem}.top nav a.hide{display:none}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

[data-t=sepia]{--bg:#f1e8d2;--card:#fbf5e6;--ink:#3b3226;--mut:#7a6b55;--bd:#e0d3b6;--sh:0 6px 24px rgba(90,70,30,.12)}
[data-t=contrast]{--bg:#000;--card:#0a0a0a;--ink:#fff;--mut:#e6e6e6;--bd:#fff;--acc:#ffe14d;--acc2:#1f1f1f;--sh:none}
[data-t=contrast] button,[data-t=contrast] .hero,[data-t=contrast] .hero h1{color:#000}[data-t=contrast] button:not(.sec):not(.chip){background:#ffe14d}[data-t=contrast] .hero{background:#ffe14d}
[data-t=dark] .acts button.on{background:#3a3000;color:#ffd666}
:focus-visible{outline:3px solid var(--acc);outline-offset:2px}
.skip{position:absolute;left:-999px;top:8px;background:var(--acc);color:#fff;padding:8px 14px;border-radius:8px;z-index:50}.skip:focus{left:8px}
#top{position:fixed;right:18px;bottom:22px;margin:0;width:44px;height:44px;padding:0;border-radius:50%;display:none;z-index:8;box-shadow:var(--sh)}
#lgw{position:relative}#lg{margin:0;display:flex;align-items:center;gap:6px;padding:6px 10px;border-radius:10px;font-size:.85rem;background:var(--acc2);color:var(--ink);font-weight:700}
.fl{width:24px;height:16px;border-radius:3px;box-shadow:0 0 0 1px rgba(0,0,0,.2);display:block;flex:none}#lgf{display:flex}
#lgm{position:absolute;right:0;top:calc(100% + 8px);background:var(--card);border:1px solid var(--bd);border-radius:14px;box-shadow:var(--sh);padding:6px;min-width:160px;z-index:25}#lgm[hidden]{display:none}
#lgm a{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:9px;text-decoration:none;color:var(--ink);font-size:.9rem}#lgm a:hover,#lgm a.on{background:var(--acc2);color:var(--acc)}
#exw{position:relative;display:inline-block}#exm{position:absolute;left:0;top:calc(100% + 6px);background:var(--card);border:1px solid var(--bd);border-radius:12px;box-shadow:var(--sh);padding:6px;min-width:210px;z-index:15}#exm[hidden]{display:none}
#exm button{display:block;width:100%;text-align:left;margin:0;border:0;background:none;color:var(--ink);padding:9px 11px;font-weight:600;font-size:.88rem}#exm button:hover{background:var(--acc2);color:var(--acc)}
#pz{margin:0;background:var(--acc2);color:var(--ink);padding:7px 11px;border-radius:10px;font-size:1rem;line-height:1}
#pzp{position:fixed;top:0;right:0;bottom:0;width:min(370px,100%);background:var(--card);color:var(--ink);border-left:1px solid var(--bd);box-shadow:-10px 0 40px rgba(0,0,0,.25);z-index:30;transform:translateX(105%);transition:transform .25s;overflow:auto;padding:18px 18px 40px}
#pzp.o{transform:none}#pzo{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:29;display:none}#pzo.o{display:block}
#pzp h3{margin:0 0 4px;font-size:1.2rem;display:flex;justify-content:space-between;align-items:center}
#pzp h3 button{margin:0;padding:4px 10px;background:var(--acc2);color:var(--ink)}
#pzp .g{margin:16px 0 4px;font-weight:700;font-size:.85rem;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}
#pzp .seg{display:flex;flex-wrap:wrap;gap:6px}#pzp .seg button{margin:0;padding:7px 11px;font-size:.85rem;background:var(--card);color:var(--ink);border:1px solid var(--bd);font-weight:600}
#pzp .seg button.on{background:var(--acc);color:#fff;border-color:var(--acc)}
#pzp .sw{display:flex;flex-wrap:wrap;gap:8px;align-items:center}#pzp .sw button{margin:0;width:32px;height:32px;padding:0;border-radius:50%;border:3px solid var(--card);box-shadow:0 0 0 1px var(--bd)}#pzp .sw button.on{box-shadow:0 0 0 3px var(--ink)}
#pzp .sw input[type=color]{width:38px;height:34px;padding:2px;border-radius:8px}
#pzp input[type=range]{padding:0;accent-color:var(--acc)}#pzp #pzr{width:100%;margin-top:18px;background:var(--acc2);color:var(--ink)}
[data-d=compact] body{line-height:1.45}[data-d=compact] .card{padding:14px;margin:10px 0}[data-d=compact] label{margin:8px 0 3px}[data-d=compact] input,[data-d=compact] select{padding:8px 10px}[data-d=compact] h2{margin:20px 0 8px}[data-d=compact] main{padding:12px 0 36px}[data-d=compact] .tool{padding:10px 12px}
[data-d=roomy] body{line-height:1.8}[data-d=roomy] .card{padding:30px;margin:24px 0}[data-d=roomy] label{margin:18px 0 7px}[data-d=roomy] input,[data-d=roomy] select{padding:15px 16px}[data-d=roomy] h2{margin:42px 0 14px}[data-d=roomy] .grid{gap:18px}
[data-w=narrow] .w{max-width:760px}[data-w=wide] .w{max-width:1240px}
[data-f=serif] body{font-family:Georgia,'Times New Roman',serif}[data-f=mono] body{font-family:ui-monospace,Consolas,Menlo,monospace}[data-f=legible] body{font-family:Verdana,Tahoma,sans-serif;letter-spacing:.02em;word-spacing:.1em}
[data-rd=sharp] :where(.card,.tool,input,select,textarea,button,details,.hero,.res div,.day,.aff,.acts button,#pzp .seg button){border-radius:3px}
[data-rd=soft] :where(.card,.tool,.hero,.day){border-radius:30px}[data-rd=soft] :where(input,select,textarea,button){border-radius:999px}
[data-v=list] .grid{grid-template-columns:1fr}[data-v=list] .tool{display:flex;gap:12px;align-items:center}[data-v=list] .tool b{margin:0}
[data-v=compact] .grid{grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px}[data-v=compact] .tool span{display:none}
[data-h=plain] .hero{background:var(--card);color:var(--ink);border:1px solid var(--bd)}[data-h=plain] .hero h1{color:var(--ink)}
[data-an=off] *{animation:none!important;transition:none!important;scroll-behavior:auto!important}
@media print{header,footer,#cb,#pzp,#pzo,#top,.acts,.ad{display:none!important}body{background:#fff;color:#000}}
"""

COMMON_JS = """
const $=id=>document.getElementById(id);
const fmt=(n,d=2)=>isFinite(n)?n.toLocaleString('es-ES',{maximumFractionDigits:d,minimumFractionDigits:0}):'—';
const eur=n=>isFinite(n)?n.toLocaleString('es-ES',{style:'currency',currency:'EUR'}):'—';
const num=id=>parseFloat(String($(id).value).replace(',','.'));
function show(items){return '<div class="res">'+items.map(i=>'<div><small>'+i[0]+'</small><b>'+i[1]+'</b></div>').join('')+'</div>'}
"""

CSS += open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'extra.css'),encoding='utf-8').read()
TOOLS = []

def tool(slug, title, h1, desc, body, js, text):
    TOOLS.append(dict(slug=slug, title=title, h1=h1, desc=desc, body=body, js=js, text=text))

# ---------------- 1 IVA ----------------
tool("calculadora-iva", "Calculadora de IVA online (21%, 10%, 4%)", "Calculadora de IVA",
 "Añade o quita el IVA a cualquier importe. Tipos de España: 21%, 10% y 4%. Gratis y al instante.",
 """<div class="row"><div><label for="a">Importe (€)</label><input id="a" inputmode="decimal" value="100"></div>
<div><label for="r">Tipo de IVA</label><select id="r"><option value="21">21% (general)</option><option value="10">10% (reducido)</option><option value="4">4% (superreducido)</option></select></div></div>
<label for="m">¿Qué quieres hacer?</label><select id="m"><option value="add">Añadir IVA (tengo el precio sin IVA)</option><option value="rem">Quitar IVA (tengo el precio con IVA)</option></select>
<button id="go">Calcular</button><div id="o"></div>""",
 """$('go').onclick=()=>{const a=num('a'),r=num('r')/100;let b,i,t;
if($('m').value==='add'){b=a;i=a*r;t=a+i}else{t=a;b=a/(1+r);i=t-b}
$('o').innerHTML=show([['Base imponible',eur(b)],['IVA',eur(i)],['Total con IVA',eur(t)]])};$('go').click();""",
 """<h2>¿Cómo se calcula el IVA?</h2><p>Para <b>añadir</b> el IVA se multiplica el precio sin IVA por 1,21 (si el tipo es el 21%). Para <b>quitarlo</b> se divide el precio final entre 1,21. En España hay tres tipos: general (21%), reducido (10%) y superreducido (4%).</p>
<p>Esta calculadora es orientativa. Para facturas o declaraciones consulta a tu gestor.</p>""")

# ---------------- 2 Porcentajes ----------------
tool("calculadora-porcentajes", "Calculadora de porcentajes: cómo calcular un % fácil", "Calculadora de porcentajes",
 "Calcula el X% de una cantidad, qué porcentaje es un número de otro y la variación porcentual.",
 """<h2>¿Cuánto es el X% de Y?</h2><div class="row"><div><label for="p1">Porcentaje (%)</label><input id="p1" inputmode="decimal" value="15"></div><div><label for="y1">De la cantidad</label><input id="y1" inputmode="decimal" value="200"></div></div><div id="o1"></div>
<h2>¿Qué porcentaje es X de Y?</h2><div class="row"><div><label for="x2">Número X</label><input id="x2" inputmode="decimal" value="30"></div><div><label for="y2">Número Y</label><input id="y2" inputmode="decimal" value="120"></div></div><div id="o2"></div>
<h2>Variación porcentual</h2><div class="row"><div><label for="v1">Valor inicial</label><input id="v1" inputmode="decimal" value="80"></div><div><label for="v2">Valor final</label><input id="v2" inputmode="decimal" value="100"></div></div><div id="o3"></div>""",
 """function c(){$('o1').innerHTML=show([['Resultado',fmt(num('p1')/100*num('y1'))]]);
$('o2').innerHTML=show([['X es el',fmt(num('x2')/num('y2')*100)+' %']]);
const v=(num('v2')-num('v1'))/Math.abs(num('v1'))*100;$('o3').innerHTML=show([['Variación',(v>0?'+':'')+fmt(v)+' %']]);}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<h2>Fórmulas básicas</h2><ul><li><b>X% de Y</b> = Y × X ÷ 100</li><li><b>Qué % es X de Y</b> = X ÷ Y × 100</li><li><b>Variación %</b> = (final − inicial) ÷ inicial × 100</li></ul>""")

# ---------------- 3 Propinas ----------------
tool("calculadora-propinas", "Calculadora de propinas y dividir la cuenta", "Calculadora de propinas y cuenta compartida",
 "Calcula la propina y cuánto paga cada persona al dividir la cuenta del restaurante.",
 """<div class="row"><div><label for="b">Total de la cuenta (€)</label><input id="b" inputmode="decimal" value="60"></div><div><label for="t">Propina (%)</label><input id="t" inputmode="decimal" value="10"></div></div>
<label for="n">Número de personas</label><input id="n" inputmode="numeric" value="4"><div id="o"></div>""",
 """function c(){const b=num('b'),t=num('t')/100,n=Math.max(1,num('n'));const tip=b*t,tot=b+tip;
$('o').innerHTML=show([['Propina',eur(tip)],['Total',eur(tot)],['Por persona',eur(tot/n)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>En España la propina no es obligatoria; lo habitual es dejar entre un 5% y un 10% si el servicio ha sido bueno. Para otros países el porcentaje habitual puede ser mayor.</p>""")

# ---------------- 4 Días entre fechas ----------------
tool("dias-entre-fechas", "Calculadora de días entre dos fechas", "Días entre dos fechas",
 "Calcula cuántos días, semanas y días laborables hay entre dos fechas.",
 """<div class="row"><div><label for="d1">Fecha inicial</label><input id="d1" type="date"></div><div><label for="d2">Fecha final</label><input id="d2" type="date"></div></div>
<button id="go">Calcular</button><div id="o"></div>""",
 """const t=new Date();$('d1').value=t.toISOString().slice(0,10);const f=new Date(t.getTime()+30*864e5);$('d2').value=f.toISOString().slice(0,10);
$('go').onclick=()=>{let a=new Date($('d1').value),b=new Date($('d2').value);if(isNaN(a)||isNaN(b)){$('o').innerHTML='<p>Elige las dos fechas.</p>';return}
if(a>b)[a,b]=[b,a];const days=Math.round((b-a)/864e5);let w=0;for(let d=new Date(a);d<b;d.setDate(d.getDate()+1)){const g=d.getDay();if(g!==0&&g!==6)w++}
$('o').innerHTML=show([['Días',fmt(days,0)],['Semanas',fmt(days/7,1)],['Meses aprox.',fmt(days/30.44,1)],['Días laborables (L-V)',fmt(w,0)]])};$('go').click();""",
 """<p>Los días laborables que se muestran son de lunes a viernes y no descuentan festivos, que varían según la comunidad autónoma y la localidad.</p>""")

# ---------------- 5 Edad ----------------
tool("calculadora-edad", "Calculadora de edad exacta: años, meses y días", "Calculadora de edad",
 "Descubre tu edad exacta en años, meses y días y cuánto falta para tu próximo cumpleaños.",
 """<label for="n">Fecha de nacimiento</label><input id="n" type="date" value="2000-01-01"><button id="go">Calcular</button><div id="o"></div>""",
 """$('go').onclick=()=>{const n=new Date($('n').value),h=new Date();if(isNaN(n)||n>h){$('o').innerHTML='<p>Introduce una fecha válida.</p>';return}
let y=h.getFullYear()-n.getFullYear(),m=h.getMonth()-n.getMonth(),d=h.getDate()-n.getDate();
if(d<0){m--;d+=new Date(h.getFullYear(),h.getMonth(),0).getDate()}if(m<0){y--;m+=12}
let nx=new Date(h.getFullYear(),n.getMonth(),n.getDate());if(nx<=new Date(h.getFullYear(),h.getMonth(),h.getDate()))nx=new Date(h.getFullYear()+1,n.getMonth(),n.getDate());
const tot=Math.floor((h-n)/864e5);
$('o').innerHTML=show([['Edad',y+' años, '+m+' meses, '+d+' días'],['Días vividos',fmt(tot,0)],['Próximo cumpleaños en',Math.ceil((nx-h)/864e5)+' días']])};$('go').click();""",
 "")

# ---------------- 6 Conversor ----------------
tool("conversor-unidades", "Conversor de unidades: longitud, peso, volumen y temperatura", "Conversor de unidades",
 "Convierte kilómetros a millas, kilos a libras, litros a galones y grados Celsius a Fahrenheit.",
 """<label for="c">Tipo</label><select id="c"></select>
<div class="row"><div><label for="v">Valor</label><input id="v" inputmode="decimal" value="1"></div><div></div></div>
<div class="row"><div><label for="f">De</label><select id="f"></select></div><div><label for="t">A</label><select id="t"></select></div></div><div id="o"></div>""",
 """const U={'Longitud':{m:1,km:1000,cm:.01,mm:.001,milla:1609.344,yarda:.9144,pie:.3048,pulgada:.0254},
'Peso':{kg:1,g:.001,mg:1e-6,tonelada:1000,libra:.45359237,onza:.028349523},
'Volumen':{litro:1,ml:.001,'m³':1000,'galón (US)':3.785411784,'taza (US)':.2365882365},
'Temperatura':{'°C':1,'°F':1,'K':1}};
const c=$('c'),f=$('f'),t=$('t');Object.keys(U).forEach(k=>c.add(new Option(k,k)));
function fill(){const k=Object.keys(U[c.value]);f.innerHTML=t.innerHTML='';k.forEach(x=>{f.add(new Option(x,x));t.add(new Option(x,x))});t.selectedIndex=Math.min(1,k.length-1);calc()}
function calc(){const v=num('v');let r;
if(c.value==='Temperatura'){let C=f.value==='°C'?v:f.value==='°F'?(v-32)*5/9:v-273.15;r=t.value==='°C'?C:t.value==='°F'?C*9/5+32:C+273.15}
else r=v*U[c.value][f.value]/U[c.value][t.value];
$('o').innerHTML=show([[fmt(v,6)+' '+f.value+' =',fmt(r,6)+' '+t.value]])}
c.onchange=fill;[f,t,$('v')].forEach(e=>e.oninput=calc);f.onchange=t.onchange=calc;fill();""",
 "")

# ---------------- 7 Contraseñas ----------------
tool("generador-contrasenas", "Generador de contraseñas seguras aleatorias", "Generador de contraseñas seguras",
 "Crea contraseñas aleatorias y seguras en tu navegador. No se envían ni se guardan en ningún sitio.",
 """<label for="l">Longitud: <b id="lv">16</b></label><input id="l" type="range" min="8" max="64" value="16">
<label><input type="checkbox" id="u" checked style="width:auto"> Mayúsculas</label><label><input type="checkbox" id="n" checked style="width:auto"> Números</label><label><input type="checkbox" id="s" checked style="width:auto"> Símbolos</label>
<button id="go">Generar</button> <button id="cp" class="sec">Copiar</button><div class="card" style="word-break:break-all;font:20px monospace" id="o"></div>""",
 """function gen(){let s='abcdefghijkmnopqrstuvwxyz';if($('u').checked)s+='ABCDEFGHJKLMNPQRSTUVWXYZ';if($('n').checked)s+='23456789';if($('s').checked)s+='!@#$%&*?-_+=';
const L=+$('l').value,a=new Uint32Array(L);crypto.getRandomValues(a);$('o').textContent=Array.from(a,x=>s[x%s.length]).join('');$('lv').textContent=L}
$('go').onclick=gen;$('l').oninput=gen;$('cp').onclick=()=>{navigator.clipboard.writeText($('o').textContent);$('cp').textContent='¡Copiada!';setTimeout(()=>$('cp').textContent='Copiar',1500)};gen();""",
 """<p>Una contraseña larga (16 o más caracteres) y única para cada servicio es la mejor defensa. Se genera con el generador criptográfico de tu navegador y nunca sale de tu dispositivo.</p>""")

# ---------------- 8 Contador palabras ----------------
tool("contador-palabras", "Contador de palabras y caracteres online", "Contador de palabras y caracteres",
 "Cuenta palabras, caracteres, frases y párrafos de tu texto y calcula el tiempo de lectura.",
 """<label for="x">Pega o escribe tu texto</label><textarea id="x" placeholder="Escribe aquí..."></textarea><div id="o"></div>""",
 """function c(){const x=$('x').value,w=(x.trim().match(/\\S+/g)||[]).length;
$('o').innerHTML=show([['Palabras',fmt(w,0)],['Caracteres',fmt(x.length,0)],['Sin espacios',fmt(x.replace(/\\s/g,'').length,0)],['Frases',fmt((x.match(/[.!?]+(\\s|$)/g)||[]).length,0)],['Párrafos',fmt(x.split(/\\n+/).filter(s=>s.trim()).length,0)],['Lectura',Math.max(w?1:0,Math.round(w/200))+' min']])}
$('x').oninput=c;c();""",
 """<p>El tiempo de lectura se estima a 200 palabras por minuto. Útil para redacciones, límites de caracteres en redes sociales, descripciones de vídeo o SEO.</p>""")

# ---------------- 9 Descuentos ----------------
tool("calculadora-descuentos", "Calculadora de descuentos y rebajas", "Calculadora de descuentos",
 "Calcula el precio final y cuánto ahorras con un descuento o rebaja (porcentaje).",
 """<div class="row"><div><label for="p">Precio original (€)</label><input id="p" inputmode="decimal" value="59,90"></div><div><label for="d">Descuento (%)</label><input id="d" inputmode="decimal" value="30"></div></div>
<label for="d2">Descuento adicional (%) — opcional</label><input id="d2" inputmode="decimal" value="0"><div id="o"></div>""",
 """function c(){const p=num('p'),a=num('d')/100,b=(num('d2')||0)/100;const f=p*(1-a)*(1-b);
$('o').innerHTML=show([['Precio final',eur(f)],['Ahorras',eur(p-f)],['Descuento total',fmt((1-f/p)*100,1)+' %']])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>Si aplicas dos descuentos seguidos, no se suman: el segundo se aplica sobre el precio ya rebajado. Por ejemplo, 30% + 10% equivale a un 37% de descuento total.</p>""")

# ---------------- 10 Hipoteca ----------------
tool("calculadora-hipoteca", "Calculadora de hipoteca: cuota mensual e intereses", "Calculadora de hipoteca",
 "Calcula la cuota mensual y el total de intereses de una hipoteca a tipo fijo.",
 """<div class="row"><div><label for="c">Capital a financiar (€)</label><input id="c" inputmode="decimal" value="150000"></div><div><label for="i">Interés anual (%)</label><input id="i" inputmode="decimal" value="3"></div></div>
<label for="y">Plazo (años)</label><input id="y" inputmode="numeric" value="25"><div id="o"></div>""",
 """function c(){const C=num('c'),r=num('i')/100/12,n=num('y')*12;const q=r===0?C/n:C*r/(1-Math.pow(1+r,-n));
$('o').innerHTML=show([['Cuota mensual',eur(q)],['Total a pagar',eur(q*n)],['Total intereses',eur(q*n-C)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>Cálculo con sistema de amortización francés (cuota constante) y tipo fijo. No incluye comisiones, seguros ni gastos de formalización. Es una simulación orientativa, no una oferta.</p>""")

# ---------------- 11 IMC ----------------
tool("calculadora-imc", "Calculadora de IMC (índice de masa corporal)", "Calculadora de IMC",
 "Calcula tu índice de masa corporal a partir de tu peso y altura y consulta la categoría según la OMS.",
 """<div class="row"><div><label for="w">Peso (kg)</label><input id="w" inputmode="decimal" value="70"></div><div><label for="h">Altura (cm)</label><input id="h" inputmode="decimal" value="170"></div></div><div id="o"></div>""",
 """function c(){const w=num('w'),h=num('h')/100,i=w/(h*h);const k=i<18.5?'Bajo peso':i<25?'Peso normal':i<30?'Sobrepeso':'Obesidad';
$('o').innerHTML=show([['Tu IMC',fmt(i,1)],['Categoría (OMS)',k]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<h2>Rangos del IMC según la OMS</h2><ul><li>Menos de 18,5: bajo peso</li><li>18,5 a 24,9: peso normal</li><li>25 a 29,9: sobrepeso</li><li>30 o más: obesidad</li></ul><p>El IMC es solo un indicador orientativo: no distingue entre músculo y grasa. Para cualquier decisión sobre tu salud consulta a un profesional sanitario.</p>""")

# ---------------- 12 Interés compuesto ----------------
tool("calculadora-interes-compuesto", "Calculadora de interés compuesto y ahorro", "Calculadora de interés compuesto",
 "Simula cuánto dinero tendrás ahorrando una cantidad cada mes con un interés anual durante varios años.",
 """<div class="row"><div><label for="i0">Capital inicial (€)</label><input id="i0" inputmode="decimal" value="1000"></div><div><label for="ap">Aportación mensual (€)</label><input id="ap" inputmode="decimal" value="100"></div></div>
<div class="row"><div><label for="r">Interés anual (%)</label><input id="r" inputmode="decimal" value="4"></div><div><label for="y">Años</label><input id="y" inputmode="numeric" value="10"></div></div><div id="o"></div>""",
 """function c(){let b=num('i0');const a=num('ap'),r=num('r')/100/12,n=Math.round(num('y')*12);for(let k=0;k<n;k++){b=b*(1+r)+a}
const put=num('i0')+a*n;$('o').innerHTML=show([['Capital final',eur(b)],['Total aportado',eur(put)],['Intereses ganados',eur(b-put)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>El interés compuesto significa que los intereses generan a su vez nuevos intereses. Cuanto antes empieces y más tiempo mantengas el ahorro, mayor es el efecto. Esta simulación supone una rentabilidad constante, algo que en la realidad no está garantizado, y no tiene en cuenta impuestos ni inflación. No es asesoramiento financiero.</p>""")

# ---------------- 13 Préstamo ----------------
tool("calculadora-prestamos", "Calculadora de préstamos personales: cuota mensual", "Calculadora de préstamos",
 "Calcula la cuota mensual y los intereses totales de un préstamo personal o de coche.",
 """<div class="row"><div><label for="c">Importe (€)</label><input id="c" inputmode="decimal" value="10000"></div><div><label for="i">Interés anual (%)</label><input id="i" inputmode="decimal" value="7"></div></div>
<label for="m">Plazo (meses)</label><input id="m" inputmode="numeric" value="48"><div id="o"></div>""",
 """function c(){const C=num('c'),r=num('i')/100/12,n=num('m');const q=r===0?C/n:C*r/(1-Math.pow(1+r,-n));
$('o').innerHTML=show([['Cuota mensual',eur(q)],['Total a devolver',eur(q*n)],['Intereses',eur(q*n-C)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>Cálculo con cuota constante. No incluye comisiones de apertura ni seguros vinculados. Compara siempre la TAE que te ofrezca cada entidad.</p>""")

# ---------------- 14 Nota media ----------------
tool("calculadora-nota-media", "Calculadora de nota media y nota que necesito en el examen", "Calculadora de nota media",
 "Calcula tu nota media ponderada y la nota que necesitas en el examen final para aprobar.",
 """<h2>Media ponderada</h2><div id="rows"></div><div id="o1"></div>
<h2>¿Qué nota necesito en el examen final?</h2><div class="row"><div><label for="a">Nota actual (0-10)</label><input id="a" inputmode="decimal" value="5,5"></div><div><label for="wa">Peso de la nota actual (%)</label><input id="wa" inputmode="decimal" value="60"></div></div>
<div class="row"><div><label for="obj">Nota que quieres sacar</label><input id="obj" inputmode="decimal" value="5"></div><div></div></div><div id="o2"></div>""",
 """const R=$('rows');for(let k=1;k<=6;k++)R.insertAdjacentHTML('beforeend','<div class="row"><div><label>Nota '+k+'</label><input class="n" inputmode="decimal"></div><div><label>Peso '+k+' (%)</label><input class="p" inputmode="decimal"></div></div>');
R.querySelectorAll('.n')[0].value='7';R.querySelectorAll('.p')[0].value='40';R.querySelectorAll('.n')[1].value='5';R.querySelectorAll('.p')[1].value='60';
function c(){const n=[...R.querySelectorAll('.n')],p=[...R.querySelectorAll('.p')];let s=0,w=0;n.forEach((x,i)=>{const a=parseFloat(x.value.replace(',','.')),b=parseFloat(p[i].value.replace(',','.'));if(isFinite(a)&&isFinite(b)){s+=a*b;w+=b}});
$('o1').innerHTML=show([['Nota media',w?fmt(s/w,2):'—'],['Peso total',fmt(w,0)+' %']]);
const need=(num('obj')-num('a')*num('wa')/100)/((100-num('wa'))/100);
$('o2').innerHTML=show([['Nota necesaria en el examen',need>10?fmt(need,2)+' (no es posible)':need<0?'0 (ya la tienes)':fmt(need,2)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 "")

# ---------------- 15 Regla de tres ----------------
tool("regla-de-tres", "Calculadora de regla de tres simple (directa e inversa)", "Calculadora de regla de tres",
 "Resuelve reglas de tres simples directas e inversas paso a paso.",
 """<label for="t">Tipo</label><select id="t"><option value="d">Directa (más → más)</option><option value="i">Inversa (más → menos)</option></select>
<div class="row"><div><label for="a">Si A</label><input id="a" inputmode="decimal" value="3"></div><div><label for="b">equivale a B</label><input id="b" inputmode="decimal" value="12"></div></div>
<div class="row"><div><label for="c">entonces C</label><input id="c" inputmode="decimal" value="5"></div><div></div></div><div id="o"></div>""",
 """function c(){const a=num('a'),b=num('b'),cc=num('c');const x=$('t').value==='d'?b*cc/a:a*b/cc;$('o').innerHTML=show([['Resultado (X)',fmt(x,4)]])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
 """<ul><li><b>Directa:</b> X = B × C ÷ A. Ejemplo: 3 kg cuestan 12 €, ¿cuánto cuestan 5 kg? 20 €.</li><li><b>Inversa:</b> X = A × B ÷ C. Ejemplo: 3 obreros tardan 12 días, ¿cuánto tardan 6? 6 días.</li></ul>""")

# ---------------- 16 Sorteo ----------------
tool("sorteo-aleatorio", "Sorteo aleatorio: elegir ganador de una lista de nombres", "Sorteo aleatorio de nombres",
 "Pega una lista de nombres (uno por línea) y elige al azar uno o varios ganadores. Ideal para sorteos en redes sociales.",
 """<label for="l">Lista de participantes (uno por línea)</label><textarea id="l" placeholder="Ana&#10;Luis&#10;Marta"></textarea>
<label for="n">Número de ganadores</label><input id="n" inputmode="numeric" value="1"><button id="go">Sortear</button><div id="o"></div>""",
 """$('go').onclick=()=>{const L=[...new Set($('l').value.split('\\n').map(s=>s.trim()).filter(Boolean))];const n=Math.min(Math.max(1,num('n')||1),L.length);
if(!L.length){$('o').innerHTML='<p>Añade al menos un nombre.</p>';return}
for(let i=L.length-1;i>0;i--){const a=new Uint32Array(1);crypto.getRandomValues(a);const j=a[0]%(i+1);[L[i],L[j]]=[L[j],L[i]]}
$('o').innerHTML='<div class="card"><b>🎉 Ganador'+(n>1?'es':'')+':</b><ol>'+L.slice(0,n).map(x=>'<li style="font-size:20px">'+x.replace(/</g,'&lt;')+'</li>').join('')+'</ol></div>'};""",
 """<p>El sorteo usa el generador aleatorio criptográfico de tu navegador y elimina nombres repetidos. Si lo haces en redes sociales, graba la pantalla del sorteo como prueba y revisa las bases legales de tu plataforma.</p>""")

# ---------------- 17 Coste viaje ----------------
tool("coste-viaje-gasolina", "Calculadora de coste de un viaje en coche (gasolina)", "Coste de un viaje en coche",
 "Calcula cuánta gasolina o diésel gastarás y cuánto cuesta un viaje, también por persona.",
 """<div class="row"><div><label for="k">Distancia (km)</label><input id="k" inputmode="decimal" value="450"></div><div><label for="c">Consumo (l/100 km)</label><input id="c" inputmode="decimal" value="6,5"></div></div>
<div class="row"><div><label for="p">Precio del litro (€)</label><input id="p" inputmode="decimal" value="1,60"></div><div><label for="n">Personas</label><input id="n" inputmode="numeric" value="3"></div></div>
<label><input type="checkbox" id="rt" style="width:auto"> Ida y vuelta</label><div id="o"></div>""",
 """function c(){let k=num('k');if($('rt').checked)k*=2;const l=k*num('c')/100,t=l*num('p');$('o').innerHTML=show([['Litros',fmt(l,1)+' l'],['Coste combustible',eur(t)],['Por persona',eur(t/Math.max(1,num('n')))]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>No incluye peajes, aparcamiento ni desgaste del vehículo. Compartir coche reparte el coste del combustible entre todos los ocupantes.</p>""")

# ---------------- 18 Horas ----------------
tool("calculadora-horas-trabajadas", "Calculadora de horas trabajadas entre dos horas", "Calculadora de horas trabajadas",
 "Calcula las horas trabajadas entre la hora de entrada y de salida, descontando el descanso.",
 """<div class="row"><div><label for="a">Entrada</label><input id="a" type="time" value="09:00"></div><div><label for="b">Salida</label><input id="b" type="time" value="17:30"></div></div>
<div class="row"><div><label for="d">Descanso (minutos)</label><input id="d" inputmode="numeric" value="30"></div><div><label for="r">Precio por hora (€) — opcional</label><input id="r" inputmode="decimal" value="0"></div></div><div id="o"></div>""",
 """function tm(s){const p=s.split(':');return +p[0]*60+ +p[1]}
function c(){let m=tm($('b').value)-tm($('a').value);if(m<0)m+=1440;m-=num('d')||0;m=Math.max(0,m);const h=m/60;
$('o').innerHTML=show([['Tiempo trabajado',Math.floor(m/60)+' h '+(m%60)+' min'],['En horas decimales',fmt(h,2)],['Importe',eur(h*(num('r')||0))]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>Si la hora de salida es menor que la de entrada se entiende que el turno cruza la medianoche.</p>""")

# ---------------- 19 Mayúsculas ----------------
tool("convertidor-mayusculas", "Convertir texto a mayúsculas, minúsculas y título", "Convertidor de mayúsculas y minúsculas",
 "Pasa tu texto a MAYÚSCULAS, minúsculas, Tipo Título o Tipo frase con un clic.",
 """<textarea id="x" placeholder="Escribe o pega tu texto..."></textarea>
<button data-m="u">MAYÚSCULAS</button> <button data-m="l" class="sec">minúsculas</button> <button data-m="t" class="sec">Tipo Título</button> <button data-m="s" class="sec">Tipo frase</button> <button id="cp" class="sec">Copiar</button>""",
 """const x=$('x');document.querySelectorAll('[data-m]').forEach(b=>b.onclick=()=>{const m=b.dataset.m,v=x.value;
x.value=m==='u'?v.toUpperCase():m==='l'?v.toLowerCase():m==='t'?v.toLowerCase().replace(/(^|\\s)(\\S)/g,(a,s,c)=>s+c.toUpperCase()):v.toLowerCase().replace(/(^|[.!?¡¿]\\s*)(\\S)/g,(a,s,c)=>s+c.toUpperCase())});
$('cp').onclick=()=>{navigator.clipboard.writeText(x.value);$('cp').textContent='¡Copiado!';setTimeout(()=>$('cp').textContent='Copiar',1500)};""",
 "")

# ---------------- 20 Margen ----------------
tool("calculadora-margen-beneficio", "Calculadora de margen y beneficio (y margen sobre coste)", "Calculadora de margen de beneficio",
 "Calcula el beneficio, el margen y el markup de un producto, o el precio de venta para ganar el margen que quieras.",
 """<h2>Tengo coste y precio de venta</h2><div class="row"><div><label for="c">Coste del producto (€)</label><input id="c" inputmode="decimal" value="12"></div><div><label for="v">Precio de venta (€)</label><input id="v" inputmode="decimal" value="25"></div></div><div id="o1"></div>
<h2>Quiero un margen concreto</h2><div class="row"><div><label for="c2">Coste (€)</label><input id="c2" inputmode="decimal" value="12"></div><div><label for="m2">Margen deseado (%)</label><input id="m2" inputmode="decimal" value="40"></div></div><div id="o2"></div>""",
 """function c(){const C=num('c'),V=num('v');$('o1').innerHTML=show([['Beneficio',eur(V-C)],['Margen sobre venta',fmt((V-C)/V*100,1)+' %'],['Markup sobre coste',fmt((V-C)/C*100,1)+' %']]);
const C2=num('c2'),m=num('m2')/100;$('o2').innerHTML=show([['Precio de venta',eur(C2/(1-m))],['Beneficio por unidad',eur(C2/(1-m)-C2)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<h2>Margen y markup no son lo mismo</h2><p>El <b>margen</b> es el beneficio dividido entre el precio de venta. El <b>markup</b> es el beneficio dividido entre el coste. Un producto que cuesta 12 € y se vende a 25 € tiene un 52% de margen y un 108% de markup. Recuerda descontar también envío, comisiones de plataforma, devoluciones y publicidad para saber tu beneficio real.</p>""")

# ---------------- 21 Letra DNI ----------------
tool("calcular-letra-dni", "Calcular la letra del DNI a partir del número", "Calculadora de la letra del DNI",
 "Introduce los 8 números de tu DNI y descubre su letra. También sirve para comprobar si un DNI es válido.",
 """<label for="n">Número del DNI (8 cifras)</label><input id="n" inputmode="numeric" maxlength="8" value="12345678"><div id="o"></div>""",
 """const L='TRWAGMYFPDXBNJZSQVHLCKE';
function c(){const v=$('n').value.replace(/\\D/g,'');if(v.length<7||v.length>8){$('o').innerHTML='<p>Introduce 7 u 8 cifras.</p>';return}
$('o').innerHTML=show([['Letra',L[parseInt(v,10)%23]],['DNI completo',v.padStart(8,'0')+L[parseInt(v,10)%23]]])}
$('n').oninput=c;c();""",
 """<h2>¿Cómo se calcula?</h2><p>La letra del DNI se obtiene dividiendo el número entre 23 y asignando una letra según el resto, de la serie TRWAGMYFPDXBNJZSQVHLCKE. Esta herramienta funciona en tu navegador y no guarda ni envía ningún dato.</p>""")

# ---------------- 22 Días Navidad ----------------
tool("dias-para-navidad", "¿Cuántos días faltan para Navidad, Nochevieja y Reyes?", "Cuenta atrás: días para Navidad",
 "Mira cuántos días faltan para Navidad, Nochevieja y el Día de Reyes.",
 """<div id="o"></div>""",
 """const h=new Date();const t0=new Date(h.getFullYear(),h.getMonth(),h.getDate());
function nx(m,d){let f=new Date(h.getFullYear(),m,d);if(f<t0)f=new Date(h.getFullYear()+1,m,d);return Math.round((f-t0)/864e5)}
$('o').innerHTML=show([['Navidad (25 dic)',nx(11,25)+' días'],['Nochevieja (31 dic)',nx(11,31)+' días'],['Reyes Magos (6 ene)',nx(0,6)+' días']]);""",
 """<p>La cuenta se calcula con la fecha de tu dispositivo. Si hoy es la fecha señalada, aparece 0 días.</p>""")

# ---------------- 23 Pintura ----------------
tool("calculadora-pintura", "Calculadora de pintura: cuántos litros necesito", "Calculadora de pintura",
 "Calcula los litros de pintura que necesitas para pintar una habitación según paredes, huecos y manos.",
 """<div class="row"><div><label for="l">Largo de la pared total (m)</label><input id="l" inputmode="decimal" value="14"></div><div><label for="h">Altura (m)</label><input id="h" inputmode="decimal" value="2,5"></div></div>
<div class="row"><div><label for="v">Puertas y ventanas (m²)</label><input id="v" inputmode="decimal" value="5"></div><div><label for="m">Manos de pintura</label><input id="m" inputmode="numeric" value="2"></div></div>
<label for="r">Rendimiento (m² por litro)</label><input id="r" inputmode="decimal" value="10"><div id="o"></div>""",
 """function c(){const a=Math.max(0,num('l')*num('h')-num('v')),l=a*num('m')/num('r');$('o').innerHTML=show([['Superficie a pintar',fmt(a,1)+' m²'],['Pintura necesaria',fmt(l,1)+' l'],['Recomendado comprar',Math.ceil(l*1.1)+' l']])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
 """<p>En "largo de la pared total" suma el largo de todas las paredes que vas a pintar (el perímetro de la habitación). El rendimiento suele aparecer en el bote; lo habitual es entre 8 y 12 m² por litro. Se recomienda un 10% extra para retoques.</p>""")

import more_tools, more_tools2, more_tools3, more_tools4
more_tools.add(tool)
more_tools2.add(tool)
more_tools3.add(tool)
more_tools4.add(tool)
from faqs import FAQS

# ======================== PLANTILLAS ========================
HEAD_JS = """(function(){try{var p=JSON.parse(localStorage.getItem("pz")||"{}"),r=document.documentElement,t=p.t||localStorage.getItem("th");if(!t||t==="auto")t=matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light";r.setAttribute("data-t",t);if(p.a){r.style.setProperty("--au",p.a);r.style.setProperty("--au2",p.b||p.a)}if(p.fs)r.style.setProperty("--fs",p.fs+"%");["d","w","f","rd","v","h","an"].forEach(function(k){if(p[k])r.setAttribute("data-"+k,p[k])})}catch(e){}})();"""

def head(title, desc, path):
    canon = f"{SITE_URL}/{path[:-5] if path.endswith('.html') else path}"
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {SITE_NAME}</title><meta name="msvalidate.01" content="4E05EBC65D30496D1F9D6D813D4F8619"><meta name="description" content="{desc}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<script>{HEAD_JS}</script><style>{CSS}</style></head><body>"""

FLAGS = {
 "es": '<svg class="fl" viewBox="0 0 24 16" aria-hidden="true"><rect width="24" height="16" fill="#c60b1e"/><rect y="4" width="24" height="8" fill="#ffc400"/></svg>',
 "ca": '<svg class="fl" viewBox="0 0 24 16" aria-hidden="true"><rect width="24" height="16" fill="#fcdd09"/>' + "".join(f'<rect y="{i*16/9:.3f}" width="24" height="{16/9:.3f}" fill="#da121a"/>' for i in (1,3,5,7)) + '</svg>',
 "va": '<svg class="fl" viewBox="0 0 24 16" aria-hidden="true"><rect width="24" height="16" fill="#fcdd09"/>' + "".join(f'<rect y="{i*16/9:.3f}" width="24" height="{16/9:.3f}" fill="#da121a"/>' for i in (1,3,5,7)) + '<rect width="7" height="16" fill="#fff"/><rect width="6" height="16" fill="#0b4ea2"/></svg>',
 "en": '<svg class="fl" viewBox="0 0 60 30" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="30" fill="#012169"/><path d="M0,0 60,30M60,0 0,30" stroke="#fff" stroke-width="6"/><path d="M0,0 60,30M60,0 0,30" stroke="#c8102e" stroke-width="2.5"/><path d="M30,0V30M0,15H60" stroke="#fff" stroke-width="10"/><path d="M30,0V30M0,15H60" stroke="#c8102e" stroke-width="6"/></svg>',
}
LANG_NAMES = {"es":"Español","ca":"Català","va":"Valencià","en":"English"}
LANGMENU = '<div id="lgw"><button id="lg" aria-haspopup="true" aria-expanded="false" aria-label="Idioma"><span id="lgf"></span><b id="lgc">ES</b> ▾</button><div id="lgm" hidden>' + "".join(f'<a href="#" data-l="{k if k!="es" else ""}" lang="{k}">{FLAGS[k]}<span>{LANG_NAMES[k]}</span></a>' for k in ("es","ca","va","en")) + '</div></div>'
HEADER = f"""<header><div class="w top"><a class="logo" href="/">Cuenta<span>lia</span></a><nav><a class="hide" href="/categoria-finanzas">Finanzas</a><a class="hide" href="/categoria-conversores">Conversores</a><a href="/">Todas</a><a class="hide" href="/mis-herramientas">⭐ Mis herramientas</a>{LANGMENU}<button id="th" title="Modo claro/oscuro" aria-label="Cambiar tema">🌙</button><button id="pz" title="Personalizar la web" aria-label="Personalizar">⚙️</button></nav></div></header>"""

SITE_JS = """
(function(){
var L=function(k,d){try{return JSON.parse(localStorage.getItem(k))||d}catch(e){return d}},S=function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
function toast(m){var t=document.getElementById('toast');if(!t){t=document.createElement('div');t.id='toast';document.body.appendChild(t)}t.textContent=m;t.className='s';clearTimeout(t._h);t._h=setTimeout(function(){t.className=''},1800)}
var lg=document.getElementById('lg'),lgm=document.getElementById('lgm');if(lg){var lm=location.pathname.match(/^\\/(ca|va|en)(\\/|$)/),cur=lm?lm[1]:'';
 lgm.querySelectorAll('a').forEach(function(a){if(a.dataset.l===cur){a.className='on';document.getElementById('lgf').innerHTML=a.querySelector('svg').outerHTML;document.getElementById('lgc').textContent=(cur||'es').toUpperCase()}
  a.onclick=function(e){e.preventDefault();var rest=location.pathname.replace(/^\\/(ca|va|en)(?=\\/|$)/,'')||'/';location.href=(a.dataset.l?'/'+a.dataset.l:'')+(a.dataset.l&&rest==='/'?'/':rest)+location.search}});
 lg.onclick=function(e){e.stopPropagation();var o=lgm.hidden;lgm.hidden=!o;lg.setAttribute('aria-expanded',o)};
 document.addEventListener('click',function(){lgm.hidden=true;lg.setAttribute('aria-expanded',false)});document.addEventListener('keydown',function(e){if(e.key==='Escape')lgm.hidden=true})}
var P=L('pz',{}),R=document.documentElement;
function apply(){var t=P.t;if(!t||t==='auto')t=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';R.setAttribute('data-t',t);
 if(P.a){R.style.setProperty('--au',P.a);R.style.setProperty('--au2',P.b||P.a)}else{R.style.removeProperty('--au');R.style.removeProperty('--au2')}
 if(P.fs&&P.fs!=100)R.style.setProperty('--fs',P.fs+'%');else R.style.removeProperty('--fs');
 ['d','w','f','rd','v','h','an'].forEach(function(k){if(P[k])R.setAttribute('data-'+k,P[k]);else R.removeAttribute('data-'+k)});ico()}
var th=document.getElementById('th');function ico(){th.textContent=R.getAttribute('data-t')==='light'||R.getAttribute('data-t')==='sepia'?'🌙':'☀️'}
th.onclick=function(){P.t=R.getAttribute('data-t')==='dark'?'light':'dark';S('pz',P);apply();build()};
var OPT=[['t','Tema',[['auto','Auto'],['light','☀️ Claro'],['dark','🌙 Oscuro'],['sepia','📖 Sepia'],['contrast','◐ Alto contraste']]],
['d','Densidad',[['compact','Compacta'],['','Cómoda'],['roomy','Amplia']]],
['w','Ancho de página',[['narrow','Estrecho'],['','Normal'],['wide','Ancho']]],
['f','Tipografía',[['','Sistema'],['serif','Serif'],['mono','Monoespaciada'],['legible','Muy legible']]],
['rd','Esquinas',[['sharp','Rectas'],['','Redondeadas'],['soft','Muy redondas']]],
['v','Vista de herramientas',[['','Tarjetas'],['list','Lista'],['compact','Compacta']]],
['h','Cabecera de portada',[['','Con degradado'],['plain','Sencilla']]],
['an','Animaciones',[['','Activadas'],['off','Desactivadas']]]];
var SW=[['#3b5bfd','#8a4dff'],['#0ea5a4','#22c55e'],['#e11d48','#f97316'],['#7c3aed','#d946ef'],['#0369a1','#06b6d4'],['#16a34a','#84cc16'],['#475569','#64748b']];
var pan=document.createElement('div'),ov=document.createElement('div');pan.id='pzp';ov.id='pzo';pan.setAttribute('role','dialog');pan.setAttribute('aria-label','Personalizar');document.body.appendChild(ov);document.body.appendChild(pan);
function build(){var h='<h3>⚙️ Personalizar <button id="pzx" aria-label="Cerrar">✕</button></h3><small style="color:var(--mut)">Se guarda en este navegador.</small>';
 h+='<div class="g">Color principal</div><div class="sw">'+SW.map(function(c){return '<button data-a="'+c[0]+'" data-b="'+c[1]+'" style="background:linear-gradient(135deg,'+c[0]+','+c[1]+')" class="'+((P.a||'#3b5bfd')===c[0]?'on':'')+'" aria-label="Color '+c[0]+'"></button>'}).join('')+'<input type="color" id="pzc" value="'+(P.a||'#3b5bfd')+'" title="Color propio"></div>';
 h+='<div class="g">Tamaño del texto: <span id="pzv">'+(P.fs||100)+'%</span></div><input type="range" id="pzf" min="85" max="150" step="5" value="'+(P.fs||100)+'">';
 OPT.forEach(function(o){h+='<div class="g">'+o[1]+'</div><div class="seg">'+o[2].map(function(v){return '<button data-k="'+o[0]+'" data-v="'+v[0]+'" class="'+((P[o[0]]||'')===v[0]||(o[0]==='t'&&!P.t&&v[0]==='auto')?'on':'')+'">'+v[1]+'</button>'}).join('')+'</div>'});
 h+='<button id="pzr">↺ Restablecer todo</button>';pan.innerHTML=h;
 pan.querySelectorAll('[data-k]').forEach(function(b){b.onclick=function(){var k=b.dataset.k,v=b.dataset.v;if(v)P[k]=v;else delete P[k];S('pz',P);apply();build()}});
 pan.querySelectorAll('[data-a]').forEach(function(b){b.onclick=function(){P.a=b.dataset.a;P.b=b.dataset.b;S('pz',P);apply();build()}});
 document.getElementById('pzc').oninput=function(e){P.a=e.target.value;P.b=e.target.value;S('pz',P);apply()};
 document.getElementById('pzf').oninput=function(e){P.fs=+e.target.value;document.getElementById('pzv').textContent=P.fs+'%';S('pz',P);apply()};
 document.getElementById('pzr').onclick=function(){P={};S('pz',P);try{localStorage.removeItem('th')}catch(e){}apply();build();toast('Ajustes restablecidos')};
 document.getElementById('pzx').onclick=close}
function open(){build();pan.classList.add('o');ov.classList.add('o')}function close(){pan.classList.remove('o');ov.classList.remove('o')}
document.getElementById('pz').onclick=open;ov.onclick=close;document.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
var mm=matchMedia('(prefers-color-scheme:dark)');if(mm.addEventListener)mm.addEventListener('change',function(){if(!P.t||P.t==='auto')apply()});
apply();
var mn=document.querySelector('main');if(mn){mn.id='main';var sk=document.createElement('a');sk.className='skip';sk.href='#main';sk.textContent='Saltar al contenido';document.body.insertBefore(sk,document.body.firstChild)}
var up=document.createElement('button');up.id='top';up.textContent='↑';up.setAttribute('aria-label','Volver arriba');up.onclick=function(){scrollTo({top:0,behavior:'smooth'})};document.body.appendChild(up);
addEventListener('scroll',function(){up.style.display=scrollY>500?'block':'none'},{passive:true});
var b=document.body,slug=b.getAttribute('data-s');
if(slug){
 var title=b.getAttribute('data-n'),h=document.querySelector('h1'),a=document.createElement('div');a.className='acts';
 a.innerHTML='<button id="fv">☆ Favorita</button><button id="cp">📋 Copiar resultado</button><button id="sh">🔗 Compartir</button><span id="exw"><button id="ex">📥 Exportar ▾</button><div id="exm" hidden><button data-f="csv">📊 Archivo CSV (Excel)</button><button data-f="txt">📄 Archivo de texto (.txt)</button><button data-f="pdf">🖨️ PDF (guardar al imprimir)</button></div></span><button id="pr">🖨️ Imprimir</button>';
 h.parentNode.insertBefore(a,h.nextSibling.nextSibling);
 var f=L('fav',[]),fv=document.getElementById('fv');function pf(){var on=f.indexOf(slug)>-1;fv.textContent=on?'★ En favoritas':'☆ Favorita';fv.className=on?'on':''}pf();
 fv.onclick=function(){var i=f.indexOf(slug);if(i>-1){f.splice(i,1);toast('Quitada de favoritas')}else{f.push(slug);toast('Añadida a favoritas ⭐')}S('fav',f);pf()};
 document.getElementById('cp').onclick=function(){var o=document.getElementById('o');var t=o?o.innerText.replace(/\\n+/g,' · ').trim():'';if(!t){toast('Haz un cálculo primero');return}var x=title+': '+t+' — '+location.href;(navigator.clipboard?navigator.clipboard.writeText(x):Promise.reject()).then(function(){toast('Resultado copiado ✔')},function(){toast('No se pudo copiar')})};
 document.getElementById('sh').onclick=function(){var u=location.href;if(navigator.share){navigator.share({title:title,url:u}).catch(function(){})}else if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){toast('Enlace copiado 🔗')})}};
 document.getElementById('pr').onclick=function(){window.print()};
 function collect(){var inp=[],res=[];document.querySelectorAll('.card label[for]').forEach(function(l){var e=document.getElementById(l.getAttribute('for'));if(!e)return;var v=e.tagName==='SELECT'?(e.selectedOptions[0]||{}).text:e.value;inp.push([l.textContent.trim(),String(v).replace(/\\s*\\n\\s*/g,' ')])});
  document.querySelectorAll('.card .res > div').forEach(function(d){var s=d.querySelector('small'),v=d.querySelector('b');if(s&&v)res.push([s.textContent.trim(),v.textContent.trim()])});
  if(!res.length){var o=document.getElementById('o');var t=o?o.innerText.trim():'';if(t)res.push(['Resultado',t])}return{inp:inp,res:res}}
 function dl(name,txt,mime){var bl=new Blob([txt],{type:mime}),u=URL.createObjectURL(bl),x=document.createElement('a');x.href=u;x.download=name;document.body.appendChild(x);x.click();setTimeout(function(){URL.revokeObjectURL(u);x.remove()},500)}
 var exm=document.getElementById('exm'),exb=document.getElementById('ex');
 exb.onclick=function(e){e.stopPropagation();exm.hidden=!exm.hidden};document.addEventListener('click',function(){exm.hidden=true});
 exm.querySelectorAll('button').forEach(function(bt){bt.onclick=function(){exm.hidden=true;var f=bt.dataset.f;if(f==='pdf'){window.print();return}
  var c=collect();if(!c.res.length){toast('Haz un cálculo primero');return}var d=new Date().toISOString().slice(0,10),nm=slug+'-'+d;
  if(f==='csv'){var q=function(s){return '"'+String(s).replace(/"/g,'""')+'"'},r=[[q('Herramienta'),q(title)],[q('Fecha'),q(d)],[q('Web'),q(location.href)],[],[q('Datos introducidos')]];
   c.inp.forEach(function(x){r.push([q(x[0]),q(x[1])])});r.push([]);r.push([q('Resultados')]);c.res.forEach(function(x){r.push([q(x[0]),q(x[1])])});
   dl(nm+'.csv','\\ufeff'+r.map(function(x){return x.join(';')}).join('\\r\\n'),'text/csv;charset=utf-8')}
  else{var t=['Herramienta: '+title,'Fecha: '+d,'Web: '+location.href,'','DATOS INTRODUCIDOS'];c.inp.forEach(function(x){t.push(x[0]+': '+x[1])});t.push('','RESULTADOS');c.res.forEach(function(x){t.push(x[0]+': '+x[1])});dl(nm+'.txt',t.join('\\r\\n'),'text/plain;charset=utf-8')}
  toast('Archivo descargado ✔')}});
 var go=document.getElementById('go');if(go&&['sorteo-aleatorio','numero-aleatorio'].indexOf(slug)<0){var tm;var rn=function(){clearTimeout(tm);tm=setTimeout(function(){go.click()},300)};document.querySelectorAll('.card input,.card select,.card textarea').forEach(function(el){el.addEventListener('input',rn);el.addEventListener('change',rn)})}

 var r=L('rec',[]).filter(function(x){return x[0]!==slug});r.unshift([slug,title]);S('rec',r.slice(0,8));
}
var all=window.TOOLS_ALL;
if(all){
 var by={};all.forEach(function(t){by[t[0]]=t});
 function sec(id,tt,list){var el=document.getElementById(id);if(!el)return;if(!list.length){el.innerHTML='';return}el.innerHTML='<h2>'+tt+'</h2><div class="grid">'+list.map(function(t){return '<a class="tool" href="/'+t[0]+'"><i>'+t[3]+'</i><b>'+t[1]+'</b></a>'}).join('')+'</div>'}
 sec('favs','⭐ Tus favoritas',L('fav',[]).map(function(s){return by[s]}).filter(Boolean));
 sec('recs','🕘 Vistas recientemente',L('rec',[]).map(function(x){return by[x[0]]}).filter(Boolean).slice(0,4));
 var d=new Date(),k=(d.getFullYear()*372+d.getMonth()*31+d.getDate())%all.length,t=all[k],dd=document.getElementById('day');
 if(dd)dd.innerHTML='<a class="day" href="/'+t[0]+'"><i style="font-size:30px;font-style:normal">'+t[3]+'</i><div><small>Herramienta del día</small><b>'+t[1]+'</b></div></a>';
 var q=document.getElementById('q'),cat='',chips=document.querySelectorAll('.chip');
 function flt(){var v=q.value.toLowerCase().trim(),n=0;document.querySelectorAll('#all .tool').forEach(function(a){var ok=(!cat||a.dataset.c===cat)&&a.textContent.toLowerCase().indexOf(v)>-1;a.style.display=ok?'':'none';if(ok)n++});
  document.querySelectorAll('#all h2').forEach(function(h){var g=h.nextElementSibling,vis=g.querySelectorAll('.tool:not([style*="none"])').length;h.style.display=g.style.display=vis?'':'none'});
  var nn=document.getElementById('none');nn.style.display=n?'none':'block'}
 q.oninput=flt;chips.forEach(function(c){c.onclick=function(){cat=c.dataset.c;chips.forEach(function(x){x.classList.toggle('on',x===c)});flt()}});
 document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus()}});
}
})();
"""

EXTRA_JS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'extra.js'),encoding='utf-8').read()
def adv_script():
    import json, advisor
    d = advisor.DATA[CUR["lang"]]
    return "window.ADV_S="+json.dumps({"loc":d["loc"],"t":d["t"],"journeys":[[j[0],j[1],j[2],j[3],j[4]] for j in d["journeys"]]},ensure_ascii=False)+";"

def footer(pre=""):
    return f"""<footer><div class="w"><a href="/privacidad">Privacidad y cookies</a><a href="/aviso-legal">Aviso legal</a><a href="/sobre-nosotros">Sobre nosotros</a><a href="/contacto">Contacto</a><p>© {datetime.date.today().year} {SITE_NAME}. Las calculadoras son orientativas.</p></div></footer>
<div id="cb"><div class="w"><p>Usamos cookies de terceros (publicidad) solo si las aceptas. <a href="/privacidad" style="color:#9db8ff">Más info</a></p><button id="ca">Aceptar</button><button id="cr" class="sec">Rechazar</button></div></div>
<script>
(function(){{var k='cc';var v=localStorage.getItem(k);var b=document.getElementById('cb');
function ads(){{{'' if not ADSENSE_ID else "var s=document.createElement('script');s.async=true;s.src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + ADSENSE_ID + "';s.crossOrigin='anonymous';document.head.appendChild(s);"}}}
if(v==='1')ads();else if(!v)b.style.display='block';
document.getElementById('ca').onclick=function(){{localStorage.setItem(k,'1');b.style.display='none';ads()}};
document.getElementById('cr').onclick=function(){{localStorage.setItem(k,'0');b.style.display='none'}};}})();
</script><script>{adv_script()}</script>{pre}<script>{SITE_JS}</script><script>{EXTRA_JS}</script></body></html>"""

def adslot():
    # Cuando tengas AdSense, pega aquí tu bloque <ins class="adsbygoogle"...> de "anuncio display"
    if not ADSENSE_ID: return ''
    return '<div class="ad"><!-- ANUNCIO: pega aquí el bloque de AdSense --></div>'

CUR = {"lang":"es","out":None}
def write(path, html):
    if CUR["lang"]!="es": html = localize(html, CUR["lang"], path)
    else: html = localize(html, "es", path)
    p = os.path.join(CUR["out"] or OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(html)

CATS = [
 ("finanzas","Finanzas","Hipotecas, préstamos, IVA, inversión y ahorro."),
 ("conversores","Conversores","Unidades, temperatura, velocidad, bases y zonas horarias."),
 ("fechas","Fechas y tiempo","Fechas, edad, horas y calendario."),
 ("matematicas","Matemáticas","Porcentajes, fracciones, estadística y geometría."),
 ("espana","España y documentos","DNI, NIE, IBAN y notas de acceso."),
 ("texto","Texto y utilidades","Contadores, mayúsculas, contraseñas y sorteos."),
 ("trabajo","Trabajo y nómina","Sueldo neto, pagas, despido, vacaciones y horas."),
 ("salud","Salud y deporte","IMC, calorías, peso ideal, carrera y embarazo."),
 ("dia-a-dia","Día a día","Pintura, gasolina, IMC y más."),
]
ASSIGN = {
 "finanzas":"calculadora-iva calculadora-descuentos calculadora-hipoteca calculadora-prestamos calculadora-interes-compuesto calculadora-margen-beneficio calculadora-roi calculadora-inflacion calculadora-ahorro-objetivo calculadora-rentabilidad-alquiler calculadora-propinas capacidad-endeudamiento-hipoteca amortizacion-anticipada-hipoteca revision-hipoteca-variable-euribor calculadora-tae calculadora-gastos-compra-vivienda cuanto-tardo-en-pagar-un-prestamo calculadora-salario-bruto-neto calculadora-indemnizacion-despido calculadora-pagas-extra",
 "conversores":"conversor-unidades kilometros-a-millas kilos-a-libras celsius-a-fahrenheit litros-a-galones centimetros-a-pulgadas kmh-a-mph conversor-binario-decimal-hexadecimal conversor-zonas-horarias numeros-romanos",
 "fechas":"dias-entre-fechas calculadora-edad calculadora-horas-trabajadas dias-para-navidad sumar-dias-a-fecha numero-de-semana",
 "matematicas":"calculadora-porcentajes regla-de-tres calculadora-fracciones calculadora-media-mediana-moda calculadora-pitagoras calculadora-area-figuras numero-aleatorio lanzar-dado-moneda calculadora-nota-media",
 "espana":"calcular-letra-dni calcular-letra-nie validador-iban calculadora-nota-acceso-universidad",
 "texto":"contador-palabras convertidor-mayusculas contador-caracteres-redes generador-contrasenas sorteo-aleatorio",
 "dia-a-dia":"calculadora-pintura coste-viaje-gasolina calculadora-imc",
}

# Reasignaciones y herramientas nuevas
def _move(slugs, dest):
    for c in list(ASSIGN):
        ASSIGN[c]=" ".join(x for x in ASSIGN[c].split() if x not in slugs)
    ASSIGN[dest]=(ASSIGN.get(dest,"")+" "+" ".join(slugs)).strip()
_move(["calculadora-indemnizacion-despido","calculadora-salario-bruto-neto","calculadora-pagas-extra","calculadora-horas-trabajadas","calculadora-vacaciones"],"trabajo")
_move(["calculadora-imc","calculadora-calorias-tmb","calculadora-peso-ideal","calculadora-ritmo-carrera","calculadora-fecha-probable-parto"],"salud")
_move(["calculadora-consumo-electrico","calculadora-consumo-combustible"],"dia-a-dia")
_move(["calculadora-ecuacion-segundo-grado"],"matematicas")
ICON = {"finanzas":"💶","conversores":"🔄","fechas":"📅","matematicas":"🧮","espana":"🇪🇸","texto":"✍️","dia-a-dia":"🏠","trabajo":"💼","salud":"💪"}

def catof(slug):
    for c,l in ASSIGN.items():
        if slug in l.split(): return c
    raise SystemExit("sin categoría: "+slug)

def jsonld(o):
    import json
    return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>'

def build_site(lang):
    cname = {c:n for c,n,_ in CATS}
    for t in TOOLS:
        t["cat"]=catof(t["slug"])
    for t in TOOLS:
        pos = TOOLS.index(t)
        same=[o for o in TOOLS if o["cat"]==t["cat"] and o is not t]
        rest=[TOOLS[(pos+k)%len(TOOLS)] for k in range(1,len(TOOLS)) if TOOLS[(pos+k)%len(TOOLS)] not in same]
        others=(same+rest)[:6]
        related = "".join(f'<a class="tool" href="/{o["slug"]}"><b>{o["h1"]}</b></a>' for o in others)
        aff = AFFILIATES.get(t["slug"], [])
        affhtml = ('<div class="aff"><b>Recursos recomendados</b><ul>' + "".join(f'<li><a href="{u}" rel="sponsored noopener" target="_blank">{x}</a></li>' for x, u in aff) + '</ul><small>Enlaces de afiliado: si compras o contratas desde ellos podemos recibir una comisión, sin coste extra para ti.</small></div>') if aff else ""
        url=f"{SITE_URL}/{t['slug']}"
        ld=[{"@context":"https://schema.org","@type":"WebApplication","name":t["h1"],"url":url,"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","inLanguage":"es","description":t["desc"],"offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"}},
            {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
              {"@type":"ListItem","position":1,"name":"Inicio","item":SITE_URL+"/"},
              {"@type":"ListItem","position":2,"name":cname[t["cat"]],"item":f"{SITE_URL}/categoria-{t['cat']}"},
              {"@type":"ListItem","position":3,"name":t["h1"],"item":url}]}]
        faq=FAQS.get(t["slug"],[])
        faqhtml=""
        if faq:
            ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
            faqhtml='<h2>Preguntas frecuentes</h2>'+"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
        crumbs=f'<nav class="bc"><a href="/">Inicio</a> › <a href="/categoria-{t["cat"]}">{cname[t["cat"]]}</a></nav>'
        html = (head(t["title"], t["desc"], t["slug"] + ".html").replace("</head>", "".join(jsonld(x) for x in ld)+"</head>").replace("<body>", '<body data-s="'+t["slug"]+'" data-n="'+t["h1"].replace('"','&quot;')+'">') + HEADER +
          f'<main><div class="w">{crumbs}<h1>{t["h1"]}</h1><p class="lead">{t["desc"]}</p><div class="card">{t["body"]}</div><div id="adv"></div>{adslot()}{affhtml}<div class="tx">{t["text"]}</div>{faqhtml}{adslot()}<h2>Otras herramientas</h2><div class="grid">{related}</div></div></main>'
          + footer().replace("</body></html>", f"<script>{COMMON_JS}\n{t['js']}</script></body></html>"))
        write(t["slug"] + ".html", html)
    # categorias
    for c,n,d in CATS:
        items=[t for t in TOOLS if t["cat"]==c]
        cards="".join(f'<a class="tool" href="/{t["slug"]}"><i>{ICON[c]}</i><b>{t["h1"]}</b><span>{t["desc"]}</span></a>' for t in items)
        write(f"categoria-{c}.html", head(f"{n}: calculadoras y herramientas gratis", d+" Gratis y sin registro.", f"categoria-{c}.html")+HEADER+f'<main><div class="w"><nav class="bc"><a href="/">Inicio</a></nav><h1>{n}</h1><p class="lead">{d}</p><div class="grid">{cards}</div>{adslot()}</div></main>'+footer())
    # portada agrupada
    import json
    sections=""
    for c,n,d in CATS:
        items=[t for t in TOOLS if t["cat"]==c]
        sections+=f'<h2>{ICON[c]} <a href="/categoria-{c}" style="text-decoration:none;color:inherit">{n}</a></h2><div class="grid">'+"".join(f'<a class="tool" data-c="{c}" href="/{t["slug"]}"><i>{ICON[c]}</i><b>{t["h1"]}</b><span>{t["desc"]}</span></a>' for t in items)+'</div>'
    chips='<button class="chip on" data-c="">Todas</button>'+"".join(f'<button class="chip" data-c="{c}">{ICON[c]} {n}</button>' for c,n,_ in CATS)
    alljs="window.TOOLS_ALL="+json.dumps([[t["slug"],t["h1"],t["cat"],ICON[t["cat"]],t["desc"]] for t in TOOLS],ensure_ascii=False)+";"
    idx = (head("Calculadoras y herramientas online gratis", "Calculadoras y herramientas online gratis en español: IVA, hipoteca, préstamos, conversor de unidades, letra del DNI y más.", "") + HEADER +
      f'<main><div class="w"><div class="hero"><h1>Calculadoras online gratis</h1><p>Rápidas, sin registro y desde el móvil. Tus datos no salen de tu navegador.</p><input id="q" placeholder="🔍 Busca: IVA, hipoteca, DNI, km a millas…   (pulsa / para buscar)" autocomplete="off"><div class="stats"><span>🧰 {len(TOOLS)} herramientas</span><span>⚡ Resultado al instante</span><span>🔒 Privado</span></div></div><div id="ai"></div><div id="day"></div><div id="favs"></div><div id="recs"></div><div class="chips">{chips}</div>{adslot()}<div id="all">{sections}</div><div class="none" id="none">😕 No hay resultados. Prueba con otra palabra.</div>{adslot()}</div></main>' + footer("<script>"+alljs+"</script>"))
    write("index.html", idx)
    # legales y confianza
    priv = (head("Política de privacidad y cookies", "Política de privacidad y cookies de " + SITE_NAME, "privacidad.html") + HEADER +
      f'''<main><div class="w"><h1>Política de privacidad y cookies</h1>
<p>Las calculadoras funcionan en tu navegador: los datos que escribes no se envían a nuestros servidores.</p>
<h2>Cookies y publicidad</h2><p>Este sitio puede mostrar publicidad de terceros (Google AdSense) y enlaces de afiliado. Estos terceros pueden usar cookies para mostrar anuncios personalizados. Solo se cargan si aceptas en el aviso de cookies. Puedes cambiar tu elección borrando los datos del sitio en tu navegador.</p>
<h2>Contacto</h2><p>Responsable: Alberto Martina Mont. Contacto: {CONTACT}</p></div></main>''' + footer())
    write("privacidad.html", priv)
    aviso = (head("Aviso legal", "Aviso legal de " + SITE_NAME, "aviso-legal.html") + HEADER +
      f'''<main><div class="w"><h1>Aviso legal</h1><p>Titular: Alberto Martina Mont. Contacto: {CONTACT}.</p>
<p>Los resultados de las calculadoras son orientativos y no sustituyen el asesoramiento profesional (fiscal, financiero o legal). No nos hacemos responsables de decisiones tomadas a partir de ellos.</p></div></main>''' + footer())
    write("aviso-legal.html", aviso)
    sobre = (head("Sobre nosotros", "Quiénes somos y por qué creamos "+SITE_NAME+": calculadoras gratuitas en español, claras y sin registro.", "sobre-nosotros.html") + HEADER +
      f'''<main><div class="w"><h1>Sobre nosotros</h1>
<p>{SITE_NAME} es un proyecto independiente creado por Alberto Martina Mont con una idea sencilla: que calcular un IVA, una cuota de hipoteca o la letra de un DNI sea rápido, gratuito y no exija registrarse.</p>
<h2>Cómo trabajamos</h2><p>Todas las calculadoras se ejecutan en tu navegador: los datos que introduces no salen de tu dispositivo. Revisamos las fórmulas y las explicamos junto a cada herramienta para que entiendas el resultado.</p>
<h2>Cómo se financia</h2><p>El sitio es gratuito. Puede incluir publicidad y enlaces de afiliado, siempre señalados, que nos ayudan a mantenerlo.</p>
<h2>Aviso</h2><p>Los resultados son orientativos y no sustituyen el consejo de un profesional.</p>
<p>¿Echas en falta una herramienta o has detectado un error? <a href="/contacto">Escríbenos</a>.</p></div></main>''' + footer())
    import json as _j
    my_js="var ALL="+_j.dumps([[t["slug"],t["h1"],ICON[t["cat"]]] for t in TOOLS],ensure_ascii=False)+""";
(function(){var by={};ALL.forEach(function(t){by[t[0]]=t});
function L(k,d){try{return JSON.parse(localStorage.getItem(k))||d}catch(e){return d}}
function S(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
function card(t,rm){return '<div class="mine"><a class="tool" href="/'+t[0]+'"><i>'+t[2]+'</i><b>'+t[1]+'</b></a>'+(rm?'<button class="sec x" data-s="'+t[0]+'" aria-label="Quitar">✕</button>':'')+'</div>'}
function draw(){var f=L('fav',[]).filter(function(s){return by[s]}),r=L('rec',[]).filter(function(x){return by[x[0]]});
document.getElementById('mf').innerHTML=f.length?'<div class="grid">'+f.map(function(s){return card(by[s],1)}).join('')+'</div>':'<p>Aún no tienes favoritas. Abre una herramienta y pulsa «☆ Favorita».</p>';
document.getElementById('mr').innerHTML=r.length?'<div class="grid">'+r.map(function(x){return card(by[x[0]],0)}).join('')+'</div>':'<p>Todavía no has visitado ninguna herramienta.</p>';
document.querySelectorAll('.x').forEach(function(b){b.onclick=function(){S('fav',L('fav',[]).filter(function(s){return s!==b.dataset.s}));draw()}})}
document.getElementById('cl').onclick=function(){S('rec',[]);draw()};
document.getElementById('ex').onclick=function(){var d={fav:L('fav',[]),pz:L('pz',{})};document.getElementById('bk').value=JSON.stringify(d)};
document.getElementById('im').onclick=function(){try{var d=JSON.parse(document.getElementById('bk').value);if(d.fav)S('fav',d.fav);if(d.pz)S('pz',d.pz);location.reload()}catch(e){alert('Copia no válida')}};
draw()})();"""
    mine=(head("Mis herramientas: favoritas y recientes", "Tus herramientas favoritas y las vistas recientemente en "+SITE_NAME+".", "mis-herramientas.html").replace("</head>","<style>.mine{position:relative}.mine .x{position:absolute;top:8px;right:8px;margin:0;padding:2px 8px;font-size:.8rem}#bk{min-height:90px;font-size:.8rem}</style></head>")+HEADER+
      '''<main><div class="w"><h1>⭐ Mis herramientas</h1><p class="lead">Tus favoritas y recientes. Se guardan solo en este navegador.</p>
<h2>Favoritas</h2><div id="mf"></div><h2>Vistas recientemente</h2><div id="mr"></div><button id="cl" class="sec">Borrar historial</button>
<h2>Copia de seguridad</h2><p>Exporta tus favoritas y tus ajustes de personalización para llevarlos a otro dispositivo: pulsa «Exportar», copia el texto y, en el otro dispositivo, pégalo aquí y pulsa «Importar».</p>
<textarea id="bk" placeholder="Aquí aparece tu copia"></textarea><div class="acts"><button id="ex">Exportar</button><button id="im" class="sec">Importar</button></div></div></main>'''+footer().replace("</body></html>","<script>"+my_js+"</script></body></html>"))
    write("mis-herramientas.html", mine)
    write("sobre-nosotros.html", sobre)
    cont = (head("Contacto", "Contacta con "+SITE_NAME+" para sugerir herramientas o comunicar errores.", "contacto.html") + HEADER +
      f'''<main><div class="w"><h1>Contacto</h1><p>Puedes escribirnos para sugerir una calculadora, avisar de un error o cualquier consulta:</p>
<p><a href="mailto:{CONTACT}"><b>{CONTACT}</b></a></p><p>Respondemos en cuanto podemos, normalmente en pocos días.</p></div></main>''' + footer())
    write("contacto.html", cont)
    # SEO (solo idioma base; el sitemap se genera al final)
    if lang=="es":
        write("cy9k2m7q4x8w1v5b.txt","cy9k2m7q4x8w1v5b")
        write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
        write("ads.txt", f"google.com, pub-{ADSENSE_ID.replace('ca-pub-','')}, DIRECT, f08c47fec0942fa0\n" if ADSENSE_ID else "# Rellena cuando tengas AdSense\n")
        write("google7462b51765c7efc9.html", "google-site-verification: google7462b51765c7efc9.html")

PAGES = ["", "mis-herramientas","sobre-nosotros","contacto","privacidad","aviso-legal"]
def localize(html, lang, path):
    if not html.lstrip().startswith("<!doctype html>"): return html
    slug = "" if path=="index.html" else path[:-5]
    if lang!="es":
        import ui
        for a,t in ui.pairs(lang): html = html.replace(a,t)
        html = re.sub(r'href="/(?!/)', f'href="/{lang}/', html)
        html = html.replace(SITE_URL+"/", f"{SITE_URL}/{lang}/")
        html = html.replace('<html lang="es"', '<html lang="%s"' % ("ca-valencia" if lang=="va" else lang))
        html = html.replace('"inLanguage": "es"', '"inLanguage": "%s"' % ("ca-valencia" if lang=="va" else lang))
        html = html.replace("'es-ES'", "'%s'" % ("en-US" if lang=="en" else "ca-ES"))
    alts = "".join(f'<link rel="alternate" hreflang="{h}" href="{SITE_URL}{pre}/{slug}">' for h,pre in [("es",""),("ca","/ca"),("ca-valencia","/va"),("en","/en")])
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{slug}">'
    return html.replace("</head>", alts+"</head>", 1)

def build():
    global TOOLS, FAQS
    import json
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    base_tools, base_faqs = TOOLS, FAQS
    CUR.update(lang="es", out=OUT); build_site("es")
    for lang in ("ca","va","en"):
        tr = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n", lang+".json"), encoding="utf-8"))
        TOOLS = [dict(t, **{k: tr[t["slug"]][k] for k in ("title","h1","desc","body","js","text")}) for t in base_tools]
        FAQS = {s: [tuple(x) for x in v["faq"]] for s, v in tr.items()}
        CUR.update(lang=lang, out=os.path.join(OUT, lang)); os.makedirs(CUR["out"])
        build_site(lang)
    TOOLS, FAQS = base_tools, base_faqs
    CUR.update(lang="es", out=OUT)
    urls = [""] + [t["slug"] for t in TOOLS] + [f"categoria-{c}" for c,_,_ in CATS] + PAGES[1:]
    loc = lambda pre,u: f"{SITE_URL}{pre}/{u}"
    sm = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{loc(pre,u)}</loc><lastmod>{TODAY}</lastmod></url>" for pre in ("","/ca","/va","/en") for u in urls) + "</urlset>"
    write("sitemap.xml", sm)
    print("OK:", len(TOOLS), "herramientas x 4 idiomas ->", os.path.abspath(OUT))

if __name__ == "__main__":
    build()

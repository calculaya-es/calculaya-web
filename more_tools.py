# Herramientas adicionales de CalculaYa (se cargan desde build.py)

def conv(tool, slug, title, h1, desc, la, lb, ua, ub, fa, fb, text):
    body = ('<div class="row"><div><label for="a">' + la + '</label><input id="a" inputmode="decimal" value="1"></div>'
            '<div><label for="b">' + lb + '</label><input id="b" inputmode="decimal"></div></div><div id="o"></div>')
    js = ("const A=x=>" + fa + ";const B=x=>" + fb + ";"
          "const r=n=>isFinite(n)?String(+n.toFixed(6)).replace('.',','):'';"
          "const UA='" + ua + "',UB='" + ub + "';"
          "function tb(){$('o').innerHTML='<h2>Tabla de conversión</h2>'+show([1,5,10,20,50,100].map(v=>[v+' '+UA,r(A(v))+' '+UB]))}"
          "$('a').oninput=()=>{$('b').value=r(A(num('a')))};$('b').oninput=()=>{$('a').value=r(B(num('b')))};"
          "$('b').value=r(A(num('a')));tb();")
    tool(slug, title, h1, desc, body, js, text)


def add(tool):
    # ---------- Conversores directos (muy buscados) ----------
    conv(tool, "kilometros-a-millas", "Convertir kilómetros a millas (km a mi)", "Kilómetros a millas",
         "Convierte kilómetros a millas y millas a kilómetros al instante, con tabla de equivalencias.",
         "Kilómetros", "Millas", "km", "mi", "x/1.609344", "x*1.609344",
         "<p>1 milla equivale a 1,609344 kilómetros. Para pasar de km a millas se divide entre 1,609344 (o se multiplica por 0,621371).</p>")
    conv(tool, "kilos-a-libras", "Convertir kilos a libras (kg a lb)", "Kilos a libras",
         "Convierte kilogramos a libras y libras a kilogramos con tabla de equivalencias.",
         "Kilogramos", "Libras", "kg", "lb", "x/0.45359237", "x*0.45359237",
         "<p>1 libra equivale a 0,45359237 kg. Para pasar de kilos a libras se multiplica por 2,20462.</p>")
    conv(tool, "celsius-a-fahrenheit", "Convertir grados Celsius a Fahrenheit (°C a °F)", "Celsius a Fahrenheit",
         "Convierte grados Celsius a Fahrenheit y Fahrenheit a Celsius con tabla de equivalencias.",
         "Grados Celsius (°C)", "Grados Fahrenheit (°F)", "°C", "°F", "x*9/5+32", "(x-32)*5/9",
         "<p>Fórmula: °F = °C × 9/5 + 32. Para el camino inverso: °C = (°F − 32) × 5/9. El agua hierve a 100 °C (212 °F) y se congela a 0 °C (32 °F).</p>")
    conv(tool, "litros-a-galones", "Convertir litros a galones (US)", "Litros a galones",
         "Convierte litros a galones estadounidenses y galones a litros con tabla de equivalencias.",
         "Litros", "Galones (US)", "l", "gal", "x/3.785411784", "x*3.785411784",
         "<p>Un galón estadounidense equivale a 3,785411784 litros. El galón imperial (Reino Unido) es distinto: 4,54609 litros.</p>")
    conv(tool, "centimetros-a-pulgadas", "Convertir centímetros a pulgadas (cm a in)", "Centímetros a pulgadas",
         "Convierte centímetros a pulgadas y pulgadas a centímetros. Útil para pantallas, tallas y medidas.",
         "Centímetros", "Pulgadas", "cm", "in", "x/2.54", "x*2.54",
         "<p>Una pulgada equivale exactamente a 2,54 cm. Las pantallas de televisores y móviles se miden en pulgadas en diagonal.</p>")
    conv(tool, "kmh-a-mph", "Convertir km/h a mph (millas por hora)", "km/h a mph",
         "Convierte kilómetros por hora a millas por hora y viceversa.",
         "Kilómetros por hora", "Millas por hora", "km/h", "mph", "x/1.609344", "x*1.609344",
         "<p>100 km/h equivalen a unas 62,14 mph. Es útil al conducir en países que usan millas, como Estados Unidos o Reino Unido.</p>")

    # ---------- Matemáticas ----------
    tool("calculadora-fracciones", "Calculadora de fracciones: sumar, restar, multiplicar y dividir", "Calculadora de fracciones",
         "Suma, resta, multiplica y divide fracciones y obtén el resultado simplificado y en decimal.",
         """<div class="row"><div><label for="n1">Numerador 1</label><input id="n1" inputmode="numeric" value="1"></div><div><label for="d1">Denominador 1</label><input id="d1" inputmode="numeric" value="2"></div></div>
<label for="op">Operación</label><select id="op"><option value="+">Sumar (+)</option><option value="-">Restar (−)</option><option value="*">Multiplicar (×)</option><option value="/">Dividir (÷)</option></select>
<div class="row"><div><label for="n2">Numerador 2</label><input id="n2" inputmode="numeric" value="1"></div><div><label for="d2">Denominador 2</label><input id="d2" inputmode="numeric" value="3"></div></div><div id="o"></div>""",
         """function g(a,b){a=Math.abs(a);b=Math.abs(b);while(b){[a,b]=[b,a%b]}return a}
function c(){const a=num('n1'),b=num('d1'),cc=num('n2'),d=num('d2'),o=$('op').value;let n,m;
if(o==='+'){n=a*d+cc*b;m=b*d}else if(o==='-'){n=a*d-cc*b;m=b*d}else if(o==='*'){n=a*cc;m=b*d}else{n=a*d;m=b*cc}
if(!m||!isFinite(n)||!isFinite(m)){$('o').innerHTML=show([['Resultado','No definido']]);return}
const k=g(n,m)||1;n/=k;m/=k;if(m<0){n=-n;m=-m}
$('o').innerHTML=show([['Fracción simplificada',n+(m===1?'':'/'+m)],['Decimal',fmt(n/m,6)]])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         "<p>Para sumar o restar se iguala el denominador; para multiplicar se multiplican numeradores y denominadores; para dividir se multiplica por la fracción inversa. El resultado se simplifica dividiendo entre el máximo común divisor.</p>")

    tool("calculadora-media-mediana-moda", "Calculadora de media, mediana y moda", "Media, mediana y moda",
         "Pega una lista de números y calcula la media, la mediana, la moda, el rango y más.",
         """<label for="x">Números (separados por espacios, saltos de línea o punto y coma)</label><textarea id="x">4 8 15 16 23 42 8</textarea><div id="o"></div>""",
         """function c(){const a=$('x').value.replace(/,/g,'.').split(/[\\s;]+/).map(parseFloat).filter(isFinite);
if(!a.length){$('o').innerHTML=show([['Resultado','—']]);return}
const s=[...a].sort((p,q)=>p-q),n=s.length,sum=a.reduce((p,q)=>p+q,0),med=n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;
const f={};a.forEach(v=>f[v]=(f[v]||0)+1);const mx=Math.max(...Object.values(f));const mo=Object.keys(f).filter(k=>f[k]===mx);
$('o').innerHTML=show([['Cantidad',n],['Suma',fmt(sum,4)],['Media',fmt(sum/n,4)],['Mediana',fmt(med,4)],['Moda',mx===1?'No hay moda':mo.join(', ')],['Mínimo',fmt(s[0],4)],['Máximo',fmt(s[n-1],4)],['Rango',fmt(s[n-1]-s[0],4)]])}
$('x').oninput=c;c();""",
         "<p>La <b>media</b> es la suma dividida entre la cantidad de datos; la <b>mediana</b> es el valor central al ordenarlos; la <b>moda</b> es el valor que más se repite.</p>")

    tool("calculadora-pitagoras", "Calculadora del teorema de Pitágoras: hipotenusa y catetos", "Calculadora del teorema de Pitágoras",
         "Calcula la hipotenusa o un cateto de un triángulo rectángulo con el teorema de Pitágoras.",
         """<label for="m">¿Qué quieres calcular?</label><select id="m"><option value="h">La hipotenusa (c)</option><option value="c">Un cateto</option></select>
<div class="row"><div><label id="l1" for="a">Cateto a</label><input id="a" inputmode="decimal" value="3"></div><div><label id="l2" for="b">Cateto b</label><input id="b" inputmode="decimal" value="4"></div></div><div id="o"></div>""",
         """function c(){const h=$('m').value==='h';$('l1').textContent=h?'Cateto a':'Hipotenusa c';$('l2').textContent=h?'Cateto b':'Cateto a';
const a=num('a'),b=num('b');let r;if(h)r=Math.sqrt(a*a+b*b);else r=a>b?Math.sqrt(a*a-b*b):NaN;
$('o').innerHTML=show([[h?'Hipotenusa':'Cateto que falta',isFinite(r)?fmt(r,4):'No válido (la hipotenusa debe ser mayor)']])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         "<p>El teorema dice que en un triángulo rectángulo a² + b² = c², donde c es la hipotenusa (el lado más largo, opuesto al ángulo recto).</p>")

    tool("calculadora-area-figuras", "Calculadora de área y perímetro: rectángulo, triángulo, círculo y trapecio", "Calculadora de áreas",
         "Calcula el área (y el perímetro cuando procede) de un rectángulo, triángulo, círculo o trapecio.",
         """<label for="f">Figura</label><select id="f"></select>
<div id="wx"><label id="lx" for="x">Base</label><input id="x" inputmode="decimal" value="5"></div>
<div id="wy"><label id="ly" for="y">Altura</label><input id="y" inputmode="decimal" value="3"></div>
<div id="wz"><label id="lz" for="z">Altura</label><input id="z" inputmode="decimal" value="2"></div><div id="o"></div>""",
         """const F={'Rectángulo':['Base','Altura',null],'Triángulo':['Base','Altura',null],'Círculo':['Radio',null,null],'Trapecio':['Base mayor','Base menor','Altura']};
Object.keys(F).forEach(k=>$('f').add(new Option(k,k)));
function c(){const f=$('f').value,L=F[f];['x','y','z'].forEach((id,i)=>{$('w'+id).style.display=L[i]?'':'none';if(L[i])$('l'+id).textContent=L[i]});
const x=num('x'),y=num('y'),z=num('z');let it;
if(f==='Rectángulo')it=[['Área',fmt(x*y)],['Perímetro',fmt(2*(x+y))]];
else if(f==='Triángulo')it=[['Área',fmt(x*y/2)]];
else if(f==='Círculo')it=[['Área',fmt(Math.PI*x*x)],['Longitud (circunferencia)',fmt(2*Math.PI*x)]];
else it=[['Área',fmt((x+y)/2*z)]];
$('o').innerHTML=show(it)}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         "<ul><li>Rectángulo: base × altura</li><li>Triángulo: base × altura ÷ 2</li><li>Círculo: π × radio²</li><li>Trapecio: (base mayor + base menor) ÷ 2 × altura</li></ul><p>Usa la misma unidad en todas las medidas; el área saldrá en esa unidad al cuadrado.</p>")

    tool("numeros-romanos", "Convertidor de números romanos a arábigos y viceversa", "Convertidor de números romanos",
         "Convierte números normales a números romanos y números romanos a normales (del 1 al 3999).",
         """<label for="x">Escribe un número (ej. 1994) o un número romano (ej. MCMXCIV)</label><input id="x" value="1994"><div id="o"></div>""",
         """const M=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
function toR(n){let s='';M.forEach(p=>{while(n>=p[0]){s+=p[1];n-=p[0]}});return s}
function fromR(s){s=s.toUpperCase();let i=0,n=0;M.forEach(p=>{while(s.substr(i,p[1].length)===p[1]){n+=p[0];i+=p[1].length}});return i===s.length&&s.length?n:NaN}
function c(){const v=$('x').value.trim();let o;
if(/^[0-9]+$/.test(v)){const n=parseInt(v,10);o=n>=1&&n<=3999?['Número romano',toR(n)]:['Número romano','Solo entre 1 y 3999']}
else if(v){const n=fromR(v);o=isFinite(n)&&toR(n)===v.toUpperCase()?['Número',String(n)]:['Número','Número romano no válido']}
else o=['Resultado','—'];$('o').innerHTML=show([o])}
$('x').oninput=c;c();""",
         "<p>Valores básicos: I=1, V=5, X=10, L=50, C=100, D=500, M=1000. Cuando una letra menor va delante de una mayor se resta (IV=4, IX=9, XC=90).</p>")

    tool("conversor-binario-decimal-hexadecimal", "Conversor de binario, decimal, octal y hexadecimal", "Conversor de bases numéricas",
         "Convierte números entre binario, octal, decimal y hexadecimal.",
         """<div class="row"><div><label for="x">Número</label><input id="x" value="255"></div><div><label for="b">Base del número</label><select id="b"><option value="10">Decimal (10)</option><option value="2">Binario (2)</option><option value="8">Octal (8)</option><option value="16">Hexadecimal (16)</option></select></div></div><div id="o"></div>""",
         """function c(){const v=$('x').value.trim().toLowerCase(),b=+$('b').value,n=parseInt(v,b);
if(!v||isNaN(n)||n.toString(b)!==v.replace(/^0+(?=.)/,'')){$('o').innerHTML=show([['Resultado','Número no válido para esa base']]);return}
$('o').innerHTML=show([['Binario',n.toString(2)],['Octal',n.toString(8)],['Decimal',n.toString(10)],['Hexadecimal',n.toString(16).toUpperCase()]])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         "<p>El sistema binario usa solo 0 y 1, y es la base de la informática. El hexadecimal usa 0-9 y A-F, y se emplea mucho para colores y direcciones de memoria.</p>")

    tool("numero-aleatorio", "Generador de números aleatorios entre dos valores", "Generador de números aleatorios",
         "Genera uno o varios números aleatorios entre un mínimo y un máximo.",
         """<div class="row"><div><label for="a">Mínimo</label><input id="a" inputmode="numeric" value="1"></div><div><label for="b">Máximo</label><input id="b" inputmode="numeric" value="100"></div></div>
<label for="n">¿Cuántos números? (máx. 100)</label><input id="n" inputmode="numeric" value="1"><button id="go">Generar</button><div id="o"></div>""",
         """function rnd(a,b){const u=new Uint32Array(1);crypto.getRandomValues(u);return a+Math.floor(u[0]/4294967296*(b-a+1))}
$('go').onclick=()=>{let a=Math.round(num('a')),b=Math.round(num('b')),n=Math.min(100,Math.max(1,Math.round(num('n'))||1));if(a>b)[a,b]=[b,a];
const r=[];for(let i=0;i<n;i++)r.push(rnd(a,b));$('o').innerHTML='<div class="card" style="font-size:24px;word-break:break-word">'+r.join(', ')+'</div>'};$('go').click();""",
         "<p>Los números se generan con el generador aleatorio de tu navegador. Pueden repetirse si pides varios.</p>")

    tool("lanzar-dado-moneda", "Lanzar un dado online o una moneda (cara o cruz)", "Lanzar dado o moneda",
         "Tira uno o varios dados de 6 caras o lanza una moneda al aire: cara o cruz.",
         """<label for="n">Número de dados</label><select id="n"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select>
<button id="d">🎲 Lanzar dados</button> <button id="m" class="sec">🪙 Lanzar moneda</button><div id="o"></div>""",
         """function rnd(a,b){const u=new Uint32Array(1);crypto.getRandomValues(u);return a+Math.floor(u[0]/4294967296*(b-a+1))}
$('d').onclick=()=>{const n=+$('n').value,r=[];for(let i=0;i<n;i++)r.push(rnd(1,6));$('o').innerHTML=show([['Resultado',r.join(' · ')],['Suma',r.reduce((a,b)=>a+b,0)]])};
$('m').onclick=()=>{$('o').innerHTML=show([['Resultado',rnd(0,1)?'Cara':'Cruz']])};$('d').click();""",
         "<p>Cada lanzamiento es independiente y tiene las mismas probabilidades: 1/6 para cada cara del dado y 50% para cara o cruz.</p>")

    # ---------- Finanzas ----------
    tool("calculadora-roi", "Calculadora de ROI: retorno de la inversión", "Calculadora de ROI",
         "Calcula el retorno de la inversión (ROI) y la rentabilidad anualizada de cualquier inversión o negocio.",
         """<div class="row"><div><label for="i">Dinero invertido (€)</label><input id="i" inputmode="decimal" value="1000"></div><div><label for="f">Valor final (€)</label><input id="f" inputmode="decimal" value="1350"></div></div>
<label for="y">Años transcurridos (opcional)</label><input id="y" inputmode="decimal" value="2"><div id="o"></div>""",
         """function c(){const i=num('i'),f=num('f'),y=num('y');const it=[['Beneficio',eur(f-i)],['ROI',fmt((f-i)/i*100,2)+' %']];
if(y>0&&f>0)it.push(['Rentabilidad anual (TAC)',fmt((Math.pow(f/i,1/y)-1)*100,2)+' %']);$('o').innerHTML=show(it)}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         "<p>ROI = (valor final − inversión) ÷ inversión × 100. La rentabilidad anual tiene en cuenta el tiempo: un 35% en 2 años equivale a un 16% anual. Resultados pasados no garantizan resultados futuros; no es asesoramiento financiero.</p>")

    tool("calculadora-inflacion", "Calculadora de inflación: cuánto vale tu dinero con el tiempo", "Calculadora de inflación",
         "Calcula cuánto poder adquisitivo pierde tu dinero con una inflación anual durante varios años.",
         """<div class="row"><div><label for="a">Cantidad (€)</label><input id="a" inputmode="decimal" value="10000"></div><div><label for="r">Inflación anual (%)</label><input id="r" inputmode="decimal" value="3"></div></div>
<label for="y">Años</label><input id="y" inputmode="numeric" value="10"><div id="o"></div>""",
         """function c(){const a=num('a'),r=num('r')/100,y=num('y');const k=Math.pow(1+r,y);
$('o').innerHTML=show([['Necesitarás para comprar lo mismo',eur(a*k)],['Tus '+fmt(a,0)+' € valdrán en poder de compra',eur(a/k)],['Pérdida de poder adquisitivo',fmt((1-1/k)*100,1)+' %']])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         "<p>La inflación hace que con la misma cantidad compres menos cosas cada año. Esta calculadora supone una inflación constante, algo que en la realidad varía.</p>")

    tool("calculadora-ahorro-objetivo", "Calculadora de ahorro: cuánto ahorrar al mes para una meta", "Calculadora de ahorro para una meta",
         "Calcula cuánto debes ahorrar cada mes para llegar a una cantidad objetivo en un plazo.",
         """<div class="row"><div><label for="g">Meta (€)</label><input id="g" inputmode="decimal" value="5000"></div><div><label for="c">Ya ahorrado (€)</label><input id="c" inputmode="decimal" value="500"></div></div>
<div class="row"><div><label for="m">Plazo (meses)</label><input id="m" inputmode="numeric" value="18"></div><div><label for="r">Interés anual (%) — opcional</label><input id="r" inputmode="decimal" value="0"></div></div><div id="o"></div>""",
         """function c(){const g=num('g'),c0=num('c'),n=num('m'),r=(num('r')||0)/100/12;let p;
if(r===0)p=(g-c0)/n;else{const k=Math.pow(1+r,n);p=(g-c0*k)*r/(k-1)}
$('o').innerHTML=show([['Ahorro mensual necesario',eur(Math.max(0,p))],['Total que aportarás',eur(Math.max(0,p)*n)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         "<p>Divide tu meta entre los meses disponibles y automatiza una transferencia el día que cobras: ahorrar primero y gastar después ayuda a cumplir el objetivo.</p>")

    tool("calculadora-rentabilidad-alquiler", "Calculadora de rentabilidad de un alquiler (bruta y neta)", "Rentabilidad de un alquiler",
         "Calcula la rentabilidad bruta y neta de comprar una vivienda para alquilarla.",
         """<div class="row"><div><label for="p">Precio de compra (€)</label><input id="p" inputmode="decimal" value="150000"></div><div><label for="gc">Gastos de compra (%)</label><input id="gc" inputmode="decimal" value="10"></div></div>
<div class="row"><div><label for="rf">Reforma (€)</label><input id="rf" inputmode="decimal" value="5000"></div><div><label for="al">Alquiler mensual (€)</label><input id="al" inputmode="decimal" value="750"></div></div>
<label for="ga">Gastos anuales: IBI, comunidad, seguro, mantenimiento (€)</label><input id="ga" inputmode="decimal" value="1800"><div id="o"></div>""",
         """function c(){const p=num('p'),gc=num('gc')/100,rf=num('rf')||0,al=num('al'),ga=num('ga')||0;const inv=p*(1+gc)+rf,anual=al*12;
$('o').innerHTML=show([['Inversión total',eur(inv)],['Rentabilidad bruta',fmt(anual/(p+rf)*100,2)+' %'],['Beneficio neto anual',eur(anual-ga)],['Rentabilidad neta',fmt((anual-ga)/inv*100,2)+' %']])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         "<p>La rentabilidad bruta divide el alquiler anual entre el precio; la neta descuenta los gastos y tiene en cuenta los costes de compra (impuestos, notaría, registro). No incluye impuestos sobre el alquiler, periodos sin inquilino ni financiación. Es orientativa.</p>")

    # ---------- España / documentos ----------
    tool("calculadora-nota-acceso-universidad", "Calculadora de la nota de acceso a la universidad (EBAU/EvAU)", "Nota de acceso a la universidad",
         "Calcula tu nota de acceso a la universidad en España: 60% bachillerato y 40% prueba de acceso.",
         """<div class="row"><div><label for="b">Nota media de Bachillerato (0-10)</label><input id="b" inputmode="decimal" value="8,2"></div><div><label for="e">Nota de la prueba de acceso (0-10)</label><input id="e" inputmode="decimal" value="7"></div></div><div id="o"></div>""",
         """function c(){const b=num('b'),e=num('e');
$('o').innerHTML=show([['Nota de acceso',e>=4?fmt(0.6*b+0.4*e,3):'La prueba debe ser ≥ 4'],['Aporte del Bachillerato (60%)',fmt(0.6*b,3)],['Aporte de la prueba (40%)',fmt(0.4*e,3)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         "<p>La nota de acceso (sobre 10) es el 60% de la media del Bachillerato más el 40% de la fase de acceso, que debe tener al menos un 4. Después se puede sumar la fase voluntaria hasta llegar a 14 puntos. Las condiciones pueden variar por comunidad y curso; consulta la normativa de tu universidad.</p>")

    tool("calcular-letra-nie", "Calcular la letra del NIE a partir del número", "Calculadora de la letra del NIE",
         "Descubre la letra de control de tu NIE (X, Y o Z seguida de 7 números).",
         """<div class="row"><div><label for="p">Letra inicial</label><select id="p"><option>X</option><option>Y</option><option>Z</option></select></div><div><label for="n">Número (7 cifras)</label><input id="n" inputmode="numeric" maxlength="7" value="1234567"></div></div><div id="o"></div>""",
         """const L='TRWAGMYFPDXBNJZSQVHLCKE';
function c(){const p=$('p').value,d=$('n').value.replace(/[^0-9]/g,'');if(d.length!==7){$('o').innerHTML='<p>Introduce 7 cifras.</p>';return}
const n=parseInt({X:'0',Y:'1',Z:'2'}[p]+d,10);$('o').innerHTML=show([['Letra de control',L[n%23]],['NIE completo',p+d+L[n%23]]])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         "<p>Para calcular la letra del NIE se sustituye la X por 0, la Y por 1 y la Z por 2, se forma un número con las 7 cifras y se divide entre 23. El resto indica la letra de la serie TRWAGMYFPDXBNJZSQVHLCKE. Funciona en tu navegador sin enviar datos.</p>")

    tool("validador-iban", "Validador de IBAN: comprobar si un IBAN es correcto", "Validador de IBAN",
         "Comprueba si el formato y los dígitos de control de un IBAN son correctos. No se guarda nada.",
         """<label for="x">IBAN</label><input id="x" value="ES91 2100 0418 4502 0005 1332" autocomplete="off"><div id="o"></div>""",
         """function c(){const s=$('x').value.replace(/[^A-Za-z0-9]/g,'').toUpperCase();
let ok=/^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$/.test(s);if(ok&&s.slice(0,2)==='ES'&&s.length!==24)ok=false;
if(ok){let m=0;const t=s.slice(4)+s.slice(0,4);for(const ch of t){const v=ch>='A'?String(ch.charCodeAt(0)-55):ch;for(const d of v){m=(m*10+ +d)%97}}ok=m===1}
$('o').innerHTML=show([['Resultado',s?(ok?'IBAN válido ✅':'IBAN no válido ❌'):'—'],['País',ok?s.slice(0,2):'—'],['Formato',ok?s.replace(/(.{4})/g,'$1 ').trim():'—']])}
$('x').oninput=c;c();""",
         "<p>Esta herramienta solo comprueba que el IBAN está bien formado (longitud, país y dígitos de control, algoritmo mod 97). No verifica que la cuenta exista ni a quién pertenece. Todo se calcula en tu navegador.</p>")

    # ---------- Redes y texto ----------
    tool("contador-caracteres-redes", "Contador de caracteres para X, Instagram, TikTok y YouTube", "Contador de caracteres para redes",
         "Cuenta los caracteres de tu texto y comprueba los límites de X, Instagram, TikTok, YouTube y meta descripción.",
         """<label for="x">Tu texto</label><textarea id="x" placeholder="Escribe o pega tu descripción, título o publicación..."></textarea><div id="o"></div>""",
         """const LM=[['X (tuit)',280],['Instagram (pie)',2200],['TikTok (descripción)',4000],['YouTube (título)',100],['YouTube (descripción)',5000],['Meta descripción SEO',160]];
function c(){const n=$('x').value.length;$('o').innerHTML=show([['Caracteres',fmt(n,0)]].concat(LM.map(l=>[l[0],n+' / '+l[1]+(n>l[1]?' ⚠️ te pasas':' ✅')])))}
$('x').oninput=c;c();""",
         "<p>Los límites son orientativos y las plataformas pueden cambiarlos. Los emojis pueden contar como más de un carácter en algunas redes.</p>")

    # ---------- Fechas y tiempo ----------
    tool("sumar-dias-a-fecha", "Calculadora de fechas: sumar o restar días, semanas, meses y años", "Sumar o restar tiempo a una fecha",
         "Suma o resta días, semanas, meses o años a una fecha y descubre qué día de la semana será.",
         """<div class="row"><div><label for="d">Fecha de partida</label><input id="d" type="date"></div><div><label for="op">Operación</label><select id="op"><option value="+">Sumar</option><option value="-">Restar</option></select></div></div>
<div class="row"><div><label for="n">Cantidad</label><input id="n" inputmode="numeric" value="90"></div><div><label for="u">Unidad</label><select id="u"><option value="d">Días</option><option value="w">Semanas</option><option value="m">Meses</option><option value="y">Años</option></select></div></div><div id="o"></div>""",
         """$('d').value=new Date().toISOString().slice(0,10);
function c(){const d=new Date($('d').value+'T12:00:00');if(isNaN(d)){$('o').innerHTML='<p>Elige una fecha.</p>';return}
const n=num('n')*($('op').value==='-'?-1:1),u=$('u').value;
if(u==='d')d.setDate(d.getDate()+n);else if(u==='w')d.setDate(d.getDate()+7*n);else if(u==='m')d.setMonth(d.getMonth()+n);else d.setFullYear(d.getFullYear()+n);
$('o').innerHTML=show([['Fecha resultante',d.toLocaleDateString('es-ES')],['Día de la semana',d.toLocaleDateString('es-ES',{weekday:'long'})],['Completa',d.toLocaleDateString('es-ES',{year:'numeric',month:'long',day:'numeric'})]])}
document.querySelectorAll('input,select').forEach(i=>{i.oninput=c;i.onchange=c});c();""",
         "<p>Útil para calcular plazos, fechas de vencimiento, periodos de prueba o cuántos días faltan para un evento.</p>")

    tool("numero-de-semana", "¿En qué semana del año estamos? Número de semana de una fecha", "Número de semana del año",
         "Consulta el número de semana ISO, el día del año y el día de la semana de cualquier fecha.",
         """<label for="d">Fecha</label><input id="d" type="date"><div id="o"></div>""",
         """$('d').value=new Date().toISOString().slice(0,10);
function c(){const p=$('d').value.split('-').map(Number);if(p.length<3||p.some(isNaN)){$('o').innerHTML='<p>Elige una fecha.</p>';return}
const t=Date.UTC(p[0],p[1]-1,p[2]),d=new Date(t);const dn=d.getUTCDay()||7;d.setUTCDate(d.getUTCDate()+4-dn);
const ys=Date.UTC(d.getUTCFullYear(),0,1),wk=Math.ceil(((d-ys)/864e5+1)/7);
$('o').innerHTML=show([['Semana ISO',wk],['Día del año',Math.round((t-Date.UTC(p[0],0,0))/864e5)],['Día de la semana',new Date(t).toLocaleDateString('es-ES',{weekday:'long',timeZone:'UTC'})]])}
$('d').oninput=$('d').onchange=c;c();""",
         "<p>Se usa la numeración ISO 8601: las semanas empiezan en lunes y la semana 1 es la que contiene el primer jueves del año. Es el sistema habitual en Europa.</p>")

    tool("conversor-zonas-horarias", "Conversor de zonas horarias: hora de España en otros países", "Conversor de zonas horarias",
         "Convierte una hora entre ciudades del mundo: España, Canarias, Londres, Nueva York, México, Argentina, Tokio y más.",
         """<label for="t">Fecha y hora</label><input id="t" type="datetime-local">
<div class="row"><div><label for="a">De</label><select id="a"></select></div><div><label for="b">A</label><select id="b"></select></div></div><div id="o"></div>""",
         """const Z=[['España peninsular','Europe/Madrid'],['Canarias','Atlantic/Canary'],['Londres','Europe/London'],['Nueva York','America/New_York'],['Chicago','America/Chicago'],['Los Ángeles','America/Los_Angeles'],['Ciudad de México','America/Mexico_City'],['Bogotá','America/Bogota'],['Buenos Aires','America/Argentina/Buenos_Aires'],['Santiago de Chile','America/Santiago'],['Dubái','Asia/Dubai'],['Delhi','Asia/Kolkata'],['Tokio','Asia/Tokyo'],['Sídney','Australia/Sydney']];
Z.forEach(z=>{$('a').add(new Option(z[0],z[1]));$('b').add(new Option(z[0],z[1]))});$('a').value='Europe/Madrid';$('b').value='America/Mexico_City';
const n=new Date();n.setMinutes(n.getMinutes()-n.getTimezoneOffset());$('t').value=n.toISOString().slice(0,16);
function off(z,ms){const p=new Intl.DateTimeFormat('en-US',{timeZone:z,hourCycle:'h23',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit'}).formatToParts(new Date(ms)),o={};p.forEach(x=>o[x.type]=x.value);return Date.UTC(o.year,o.month-1,o.day,o.hour,o.minute,o.second)-ms}
function c(){const v=$('t').value;if(!v){return}const q=v.split(/[-T:]/).map(Number),t0=Date.UTC(q[0],q[1]-1,q[2],q[3],q[4]);
const za=$('a').value,zb=$('b').value;const inst=t0-off(za,t0-off(za,t0));
$('o').innerHTML=show([['Hora en destino',new Date(inst).toLocaleString('es-ES',{timeZone:zb,dateStyle:'full',timeStyle:'short'})]])}
document.querySelectorAll('input,select').forEach(i=>{i.oninput=c;i.onchange=c});c();""",
         "<p>La conversión tiene en cuenta el horario de verano de cada zona. España peninsular usa CET (UTC+1) en invierno y CEST (UTC+2) en verano; Canarias va una hora por detrás.</p>")

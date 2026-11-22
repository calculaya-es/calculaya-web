# Herramientas nuevas: salud, trabajo, hogar y matemáticas

def add(tool):
    tool("calculadora-calorias-tmb", "Calculadora de calorías diarias y metabolismo basal (TMB)", "Calorías diarias y metabolismo basal",
         "Estima tu metabolismo basal y las calorías que gastas al día según tu edad, peso, altura y nivel de actividad.",
         """<div class="row"><div><label for="s">Sexo</label><select id="s"><option value="h">Hombre</option><option value="m">Mujer</option></select></div><div><label for="e">Edad (años)</label><input id="e" inputmode="numeric" value="35"></div></div>
<div class="row"><div><label for="p">Peso (kg)</label><input id="p" inputmode="decimal" value="72"></div><div><label for="a">Altura (cm)</label><input id="a" inputmode="decimal" value="172"></div></div>
<label for="f">Nivel de actividad</label><select id="f"><option value="1.2">Sedentario (poco o ningún ejercicio)</option><option value="1.375">Ligero (1-3 días/semana)</option><option value="1.55" selected>Moderado (3-5 días/semana)</option><option value="1.725">Intenso (6-7 días/semana)</option><option value="1.9">Muy intenso (trabajo físico o doble sesión)</option></select><div id="o"></div>""",
         """function c(){const t=10*num('p')+6.25*num('a')-5*num('e')+($('s').value==='h'?5:-161),m=t*num('f');
$('o').innerHTML=show([['Metabolismo basal (TMB)',fmt(t,0)+' kcal'],['Gasto diario total',fmt(m,0)+' kcal'],['Para perder peso (-15%)',fmt(m*.85,0)+' kcal'],['Para ganar peso (+10%)',fmt(m*1.1,0)+' kcal']])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         """<h2>Cómo se calcula</h2><p>Se usa la ecuación de Mifflin-St Jeor: 10 × peso (kg) + 6,25 × altura (cm) − 5 × edad + 5 (hombres) o − 161 (mujeres). El resultado es el metabolismo basal, las calorías que gasta tu cuerpo en reposo, y se multiplica por un factor según tu actividad.</p><p>Es una estimación general y no sustituye el consejo de un médico o dietista.</p>""")

    tool("calculadora-peso-ideal", "Calculadora de peso ideal según altura y sexo", "Peso ideal",
         "Calcula un rango de peso saludable según tu altura mediante el IMC y la fórmula de Devine.",
         """<div class="row"><div><label for="s">Sexo</label><select id="s"><option value="h">Hombre</option><option value="m">Mujer</option></select></div><div><label for="a">Altura (cm)</label><input id="a" inputmode="decimal" value="170"></div></div><div id="o"></div>""",
         """function c(){const a=num('a'),m=a/100,i=Math.max(0,a/2.54-60),dv=($('s').value==='h'?50:45.5)+2.3*i;
$('o').innerHTML=show([['Rango saludable (IMC 18,5-24,9)',fmt(18.5*m*m,1)+' - '+fmt(24.9*m*m,1)+' kg'],['Fórmula de Devine',fmt(dv,1)+' kg']])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         """<p>El rango saludable se obtiene con el IMC recomendado por la OMS (entre 18,5 y 24,9). La fórmula de Devine es una referencia clásica basada solo en altura y sexo. Ninguna tiene en cuenta tu masa muscular ni tu constitución, así que son orientativas.</p>""")

    tool("calculadora-ritmo-carrera", "Calculadora de ritmo de carrera: min/km, km/h y tiempo final", "Ritmo de carrera",
         "Calcula tu ritmo por kilómetro y tu velocidad media a partir de la distancia y el tiempo.",
         """<label for="d">Distancia (km)</label><input id="d" inputmode="decimal" value="10">
<div class="row"><div><label for="h">Horas</label><input id="h" inputmode="numeric" value="0"></div><div><label for="mi">Minutos</label><input id="mi" inputmode="numeric" value="55"></div></div>
<label for="se">Segundos</label><input id="se" inputmode="numeric" value="0"><div id="o"></div>""",
         """function c(){const d=num('d'),t=(num('h')||0)*3600+(num('mi')||0)*60+(num('se')||0),p=t/d,pm=Math.floor(p/60),ps=Math.round(p%60);
const pad=n=>String(n).padStart(2,'0');const f=(x,n)=>{const s=Math.round(x*n);return Math.floor(s/3600)+':'+pad(Math.floor(s%3600/60))+':'+pad(s%60)};
$('o').innerHTML=show([['Ritmo',pm+':'+pad(ps===60?0:ps)+' min/km'],['Velocidad',fmt(d/(t/3600),2)+' km/h'],['Tiempo en 5 km',f(p,5)],['Tiempo en 10 km',f(p,10)],['Media maratón',f(p,21.0975)],['Maratón',f(p,42.195)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>El ritmo es el tiempo que tardas en recorrer un kilómetro. Los tiempos de 5 km, 10 km, media maratón y maratón se calculan suponiendo que mantienes el mismo ritmo, algo que en distancias largas no siempre ocurre.</p>""")

    tool("calculadora-fecha-probable-parto", "Calculadora de fecha probable de parto y semanas de embarazo", "Fecha probable de parto",
         "Calcula la fecha probable de parto y las semanas de embarazo a partir de la fecha de tu última regla.",
         """<label for="f">Primer día de la última regla</label><input id="f" type="date"><button id="go">Calcular</button><div id="o"></div>""",
         """const t=new Date();t.setDate(t.getDate()-70);$('f').value=t.toISOString().slice(0,10);
$('go').onclick=()=>{const a=new Date($('f').value);if(isNaN(a)){$('o').innerHTML='<p>Elige una fecha.</p>';return}
const p=new Date(a.getTime()+280*864e5),d=Math.floor((new Date()-a)/864e5),fm=x=>x.toLocaleDateString('es-ES',{day:'numeric',month:'long',year:'numeric'});
$('o').innerHTML=show([['Fecha probable de parto',fm(p)],['Semanas de embarazo',d>=0?Math.floor(d/7)+' semanas y '+(d%7)+' días':'—'],['Fin del primer trimestre',fm(new Date(a.getTime()+91*864e5))]])};$('go').click();""",
         """<p>Se aplica la regla de Naegele: fecha de la última regla más 280 días (40 semanas), suponiendo ciclos de 28 días. Solo una pequeña parte de los bebés nace exactamente en esa fecha. Es una estimación: tu médico o matrona la confirmará con la ecografía.</p>""")

    tool("calculadora-vacaciones", "Calculadora de vacaciones: días devengados según tu contrato", "Vacaciones devengadas",
         "Calcula cuántos días de vacaciones te corresponden según los días trabajados en el año.",
         """<div class="row"><div><label for="v">Días de vacaciones al año</label><input id="v" inputmode="numeric" value="30"></div><div><label for="d">Días trabajados en el año</label><input id="d" inputmode="numeric" value="200"></div></div>
<div class="row"><div><label for="u">Días ya disfrutados</label><input id="u" inputmode="numeric" value="5"></div><div><label for="s">Salario bruto anual (€)</label><input id="s" inputmode="decimal" value="24000"></div></div><div id="o"></div>""",
         """function c(){const g=num('v')*Math.min(num('d'),365)/365,r=g-num('u'),dia=num('s')/365;
$('o').innerHTML=show([['Vacaciones devengadas',fmt(g,2)+' días'],['Pendientes de disfrutar',fmt(r,2)+' días'],['Valor aprox. pendientes',eur(Math.max(r,0)*dia)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>El Estatuto de los Trabajadores fija un mínimo de 30 días naturales de vacaciones al año (unos 22 laborables). Si no has trabajado el año completo, se calculan en proporción. Tu convenio colectivo o contrato pueden mejorar esos días, así que revisa ambos. El valor en euros usa el salario diario bruto y es solo orientativo.</p>""")

    tool("calculadora-consumo-electrico", "Calculadora de consumo eléctrico de electrodomésticos (kWh y €)", "Consumo eléctrico de un aparato",
         "Calcula cuánta electricidad gasta un electrodoméstico y cuánto cuesta al mes según su potencia, horas de uso y precio del kWh.",
         """<div class="row"><div><label for="w">Potencia (vatios)</label><input id="w" inputmode="decimal" value="1500"></div><div><label for="h">Horas de uso al día</label><input id="h" inputmode="decimal" value="2"></div></div>
<div class="row"><div><label for="d">Días de uso al mes</label><input id="d" inputmode="numeric" value="30"></div><div><label for="p">Precio del kWh (€)</label><input id="p" inputmode="decimal" value="0,15"></div></div><div id="o"></div>""",
         """function c(){const k=num('w')/1000*num('h'),m=k*num('d');$('o').innerHTML=show([['Consumo diario',fmt(k,2)+' kWh'],['Consumo mensual',fmt(m,1)+' kWh'],['Coste al mes',eur(m*num('p'))],['Coste al año',eur(m*num('p')*12)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>La energía se mide en kilovatios hora (kWh): potencia en kW multiplicada por las horas de uso. La potencia figura en la etiqueta del aparato. Pon el precio del kWh de tu factura y recuerda que el coste real también incluye el término de potencia, impuestos y alquiler del contador.</p>""")

    tool("calculadora-consumo-combustible", "Calculadora de consumo de combustible (l/100 km)", "Consumo del coche en l/100 km",
         "Calcula el consumo medio de tu coche en litros cada 100 km y lo que gastas por kilómetro.",
         """<div class="row"><div><label for="k">Kilómetros recorridos</label><input id="k" inputmode="decimal" value="520"></div><div><label for="l">Litros repostados</label><input id="l" inputmode="decimal" value="31"></div></div>
<label for="p">Precio del litro (€)</label><input id="p" inputmode="decimal" value="1,55"><div id="o"></div>""",
         """function c(){const k=num('k'),l=num('l'),p=num('p');$('o').innerHTML=show([['Consumo',fmt(l/k*100,2)+' l/100 km'],['Kilómetros por litro',fmt(k/l,2)+' km/l'],['Coste por 100 km',eur(l/k*100*p)],['Coste por km',eur(l/k*p)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>Para un dato fiable, llena el depósito, anota el cuentakilómetros, recorre un buen tramo y vuelve a llenarlo hasta el tope: los litros que entren son los consumidos en esos kilómetros.</p>""")

    tool("calculadora-ecuacion-segundo-grado", "Calculadora de ecuaciones de segundo grado (paso a paso)", "Ecuación de segundo grado",
         "Resuelve ax² + bx + c = 0 y obtiene las soluciones y el discriminante.",
         """<div class="row"><div><label for="a">a</label><input id="a" inputmode="decimal" value="1"></div><div><label for="b">b</label><input id="b" inputmode="decimal" value="-3"></div></div>
<label for="c">c</label><input id="c" inputmode="decimal" value="2"><div id="o"></div>""",
         """function c(){const a=num('a'),b=num('b'),cc=num('c');if(!a){$('o').innerHTML='<p>El coeficiente a no puede ser 0.</p>';return}
const D=b*b-4*a*cc;let r;if(D>0){r=[['x₁',fmt((-b+Math.sqrt(D))/(2*a),4)],['x₂',fmt((-b-Math.sqrt(D))/(2*a),4)]]}else if(D===0){r=[['Solución doble',fmt(-b/(2*a),4)]]}else{const re=fmt(-b/(2*a),4),im=fmt(Math.sqrt(-D)/(2*a),4);r=[['x₁',re+' + '+im+'i'],['x₂',re+' − '+im+'i']]}
$('o').innerHTML=show([['Discriminante',fmt(D,4)]].concat(r))}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<h2>Fórmula general</h2><p>Para ax² + bx + c = 0 las soluciones son x = (−b ± √(b² − 4ac)) / 2a. El discriminante b² − 4ac indica cuántas soluciones reales hay: dos si es positivo, una doble si es cero y ninguna real (dos complejas) si es negativo.</p>""")

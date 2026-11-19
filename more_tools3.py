# Herramientas laborales de alta búsqueda en España

def add(tool):
    tool("calculadora-indemnizacion-despido", "Calculadora de indemnización por despido (improcedente y objetivo)", "Indemnización por despido",
         "Calcula la indemnización aproximada por despido improcedente (33 días por año) u objetivo (20 días por año) a partir de tu salario y antigüedad.",
         """<div class="row"><div><label for="s">Salario bruto anual (€)</label><input id="s" inputmode="decimal" value="24000"></div><div><label for="y">Años trabajados</label><input id="y" inputmode="numeric" value="5"></div></div>
<div class="row"><div><label for="m">Meses sueltos adicionales</label><input id="m" inputmode="numeric" value="0"></div><div><label for="t">Tipo de despido</label><select id="t"><option value="imp">Improcedente (33 días/año, máx. 24 mensualidades)</option><option value="obj">Objetivo (20 días/año, máx. 12 mensualidades)</option></select></div></div><div id="o"></div>""",
         """function c(){const s=num('s'),a=(num('y')||0)+(num('m')||0)/12,imp=$('t').value==='imp';const d=s/365,dias=imp?33:20,tope=(imp?24:12)*s/12;
const bruta=d*dias*a,ind=Math.min(bruta,tope);
$('o').innerHTML=show([['Salario diario',eur(d)],['Antigüedad',fmt(a,2)+' años'],['Indemnización calculada',eur(bruta)],['Indemnización (con tope)',eur(ind)],['Tope aplicado',bruta>tope?'Sí ('+eur(tope)+')':'No']])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         """<h2>Cómo se calcula</h2><p>Para contratos posteriores a febrero de 2012, el despido improcedente se indemniza con 33 días de salario por año trabajado (los meses se prorratean) con un máximo de 24 mensualidades. En el despido objetivo son 20 días por año con un máximo de 12 mensualidades.</p><p>Si tu relación laboral empezó antes del 12 de febrero de 2012, ese periodo se calcula a 45 días por año, así que esta calculadora no sería exacta. Es una estimación orientativa: consulta con un abogado laboralista o con tu sindicato antes de firmar un finiquito.</p>""")

    tool("calculadora-salario-bruto-neto", "Calculadora de sueldo neto: de bruto anual a neto mensual (España)", "Sueldo bruto a neto",
         "Estima tu sueldo neto mensual en España a partir del bruto anual, descontando Seguridad Social e IRPF de forma aproximada.",
         """<div class="row"><div><label for="b">Salario bruto anual (€)</label><input id="b" inputmode="decimal" value="30000"></div><div><label for="p">Número de pagas</label><select id="p"><option value="14">14 pagas</option><option value="12">12 pagas (prorrateadas)</option></select></div></div><div id="o"></div>""",
         """function irpf(x){const t=[[12450,.19],[20200,.24],[35200,.30],[60000,.37],[1e12,.45]];let r=0,prev=0;for(const[l,p]of t){if(x>prev)r+=(Math.min(x,l)-prev)*p;prev=l}return r}
function c(){const b=num('b'),n=parseInt($('p').value);const ss=Math.min(b,58914)*0.065;const base=Math.max(0,b-ss-2000);
const cuota=Math.max(0,irpf(base)-irpf(5550));const neto=b-ss-cuota;
$('o').innerHTML=show([['Seguridad Social (aprox.)',eur(ss)],['IRPF (aprox.)',eur(cuota)],['Tipo medio IRPF',fmt(cuota/b*100,1)+' %'],['Neto anual',eur(neto)],['Neto al mes ('+n+' pagas)',eur(neto/n)]])}
document.querySelectorAll('input,select').forEach(i=>i.oninput=c);c();""",
         """<p>Esta calculadora aplica una escala de IRPF media estatal más autonómica, el mínimo personal de 5.550 € y una cotización de empleado de aproximadamente el 6,5%, sin hijos ni otras circunstancias personales. Tu nómina real puede variar según tu comunidad autónoma, tu situación familiar, el tipo de contrato y la retención que indique tu empresa.</p><p>Úsala solo como referencia para comparar ofertas.</p>""")

    tool("calculadora-pagas-extra", "Calculadora de pagas extra: sueldo mensual con 12 o 14 pagas", "Pagas extra: 12 o 14 pagas",
         "Convierte un salario anual en mensual con 12 pagas (prorrateadas) o con 14 pagas, y descubre cuánto cobras en cada paga.",
         """<div class="row"><div><label for="a">Salario anual (€)</label><input id="a" inputmode="decimal" value="21000"></div></div><div id="o"></div>""",
         """function c(){const a=num('a');$('o').innerHTML=show([['Con 12 pagas',eur(a/12)+' al mes'],['Con 14 pagas: cada mensual',eur(a/14)],['Con 14 pagas: cada extra',eur(a/14)],['Diferencia mes normal',eur(a/12-a/14)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>El salario anual es el mismo con 12 que con 14 pagas: cambia cómo se reparte. Con 14 pagas cobras dos pagas extra (normalmente en verano y Navidad) y cada mes es menor; con pagas prorrateadas las extras se reparten entre los 12 meses.</p>""")

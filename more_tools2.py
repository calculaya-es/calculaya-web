# Herramientas financieras de alta intención (hipotecas y préstamos)

def add(tool):
    tool("capacidad-endeudamiento-hipoteca", "¿Cuánta hipoteca me pueden dar? Calculadora de capacidad de endeudamiento", "¿Cuánta hipoteca me pueden dar?",
         "Calcula la cuota máxima, el préstamo máximo y el precio aproximado de vivienda que podrías permitirte según tus ingresos.",
         """<div class="row"><div><label for="i">Ingresos netos mensuales (€)</label><input id="i" inputmode="decimal" value="2500"></div><div><label for="d">Otras cuotas de deudas al mes (€)</label><input id="d" inputmode="decimal" value="150"></div></div>
<div class="row"><div><label for="r">Interés anual (%)</label><input id="r" inputmode="decimal" value="3"></div><div><label for="y">Plazo (años)</label><input id="y" inputmode="numeric" value="30"></div></div>
<div class="row"><div><label for="e">Endeudamiento máximo (%)</label><input id="e" inputmode="decimal" value="35"></div><div><label for="f">Financiación sobre el precio (%)</label><input id="f" inputmode="decimal" value="80"></div></div><div id="o"></div>""",
         """function c(){const ing=num('i'),deu=num('d')||0,r=num('r')/100/12,n=num('y')*12,e=num('e')/100,f=num('f')/100;
const q=Math.max(0,ing*e-deu);const P=r===0?q*n:q*(1-Math.pow(1+r,-n))/r;const precio=f>0?P/f:0;
$('o').innerHTML=show([['Cuota máxima mensual',eur(q)],['Préstamo máximo aproximado',eur(P)],['Precio de vivienda aproximado',eur(precio)],['Ahorro necesario (entrada + ~10% gastos)',eur(precio*(1-f)+precio*0.1)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<h2>La regla del 35%</h2><p>Los bancos suelen limitar la cuota de la hipoteca, sumada a tus otras deudas, a un 30-35% de tus ingresos netos. Además suelen financiar hasta el 80% del valor de tasación, por lo que tendrás que aportar la entrada y los gastos de compra con ahorros propios.</p><p>Es una estimación orientativa: cada entidad estudia tu caso (tipo de contrato, antigüedad, avalistas, historial) y puede aprobar más o menos.</p>""")

    tool("amortizacion-anticipada-hipoteca", "Calculadora de amortización anticipada: reducir cuota o plazo", "Amortización anticipada de hipoteca",
         "Compara qué ahorras en intereses al amortizar parte de tu hipoteca reduciendo la cuota o reduciendo el plazo.",
         """<div class="row"><div><label for="c">Capital pendiente (€)</label><input id="c" inputmode="decimal" value="120000"></div><div><label for="r">Interés anual (%)</label><input id="r" inputmode="decimal" value="3"></div></div>
<div class="row"><div><label for="y">Años restantes</label><input id="y" inputmode="numeric" value="22"></div><div><label for="x">Cantidad a amortizar (€)</label><input id="x" inputmode="decimal" value="10000"></div></div><div id="o"></div>""",
         """function c(){const C=num('c'),r=num('r')/100/12,n=Math.round(num('y')*12),x=num('x');const pm=(cap,m)=>r===0?cap/m:cap*r/(1-Math.pow(1+r,-m));
const q=pm(C,n),int0=q*n-C,C2=C-x;if(C2<=0||!isFinite(q)){$('o').innerHTML=show([['Resultado','La cantidad debe ser menor que el capital']]);return}
const q2=pm(C2,n),intA=q2*n-C2;const n2=r===0?C2/q:-Math.log(1-C2*r/q)/Math.log(1+r);const intB=q*n2-C2;
$('o').innerHTML=show([['Cuota actual',eur(q)],['Opción A: nueva cuota',eur(q2)],['A: ahorro en intereses',eur(int0-intA)],['Opción B: nuevo plazo',Math.floor(n2/12)+' años y '+Math.round(n2%12)+' meses'],['B: ahorro en intereses',eur(int0-intB)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>Amortizar reduciendo el <b>plazo</b> suele ahorrar más intereses totales, porque sigues pagando la misma cuota. Reducir la <b>cuota</b> te da más holgura mensual. Comprueba la comisión de amortización anticipada de tu contrato, que puede restar parte del ahorro.</p>""")

    tool("revision-hipoteca-variable-euribor", "Calculadora de revisión de hipoteca variable: nueva cuota con el Euríbor", "Revisión de hipoteca variable",
         "Calcula la cuota de tu hipoteca variable con el Euríbor y el diferencial, y simula cómo cambia si el Euríbor sube o baja.",
         """<div class="row"><div><label for="c">Capital pendiente (€)</label><input id="c" inputmode="decimal" value="140000"></div><div><label for="y">Años restantes</label><input id="y" inputmode="numeric" value="25"></div></div>
<div class="row"><div><label for="e">Euríbor (%)</label><input id="e" inputmode="decimal" value="2,5"></div><div><label for="d">Diferencial (%)</label><input id="d" inputmode="decimal" value="0,8"></div></div><div id="o"></div>""",
         """function pm(C,i,n){const r=i/100/12;return r===0?C/n:C*r/(1-Math.pow(1+r,-n))}
function c(){const C=num('c'),n=Math.round(num('y')*12),e=num('e'),d=num('d');const q=pm(C,e+d,n);
const rows=[-1,-0.5,0.5,1].map(s=>[(s>0?'Euríbor +':'Euríbor ')+fmt(s,1)+' pts',eur(pm(C,Math.max(0,e+s)+d,n))]);
$('o').innerHTML=show([['Interés aplicado',fmt(e+d,2)+' %'],['Cuota mensual',eur(q)]].concat(rows))}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>En una hipoteca variable el interés es el Euríbor más un diferencial fijo. Se revisa cada 6 o 12 meses según tu contrato; usa el valor que figure en la notificación de tu banco. El cálculo supone cuota constante hasta la siguiente revisión.</p>""")

    tool("calculadora-tae", "Calculadora de TAE: coste real de un préstamo o hipoteca", "Calculadora de TAE",
         "Calcula la TAE aproximada de un préstamo a partir del TIN, la comisión de apertura y el plazo.",
         """<div class="row"><div><label for="c">Importe (€)</label><input id="c" inputmode="decimal" value="10000"></div><div><label for="t">TIN (%)</label><input id="t" inputmode="decimal" value="6"></div></div>
<div class="row"><div><label for="m">Plazo (meses)</label><input id="m" inputmode="numeric" value="48"></div><div><label for="f">Comisión de apertura (%)</label><input id="f" inputmode="decimal" value="1"></div></div><div id="o"></div>""",
         """function c(){const C=num('c'),r=num('t')/100/12,n=Math.round(num('m')),f=num('f')/100;
const q=r===0?C/n:C*r/(1-Math.pow(1+r,-n));const rec=C*(1-f);
function v(i){let s=0;for(let k=1;k<=n;k++)s+=q/Math.pow(1+i,k);return s-rec}
let lo=0,hi=1;for(let k=0;k<80;k++){const mid=(lo+hi)/2;if(v(mid)>0)lo=mid;else hi=mid}
const tae=Math.pow(1+lo,12)-1;
$('o').innerHTML=show([['TAE aproximada',fmt(tae*100,2)+' %'],['TIN',fmt(num('t'),2)+' %'],['Cuota mensual',eur(q)],['Coste total (intereses + comisión)',eur(q*n-rec)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>El <b>TIN</b> es el interés nominal; la <b>TAE</b> incluye además las comisiones y la frecuencia de pago, por eso permite comparar ofertas. Esta calculadora incluye la comisión de apertura; no recoge seguros vinculados ni otras comisiones, que elevarían la TAE real.</p>""")

    tool("calculadora-gastos-compra-vivienda", "Calculadora de gastos de compra de una vivienda (impuestos, notaría y registro)", "Gastos de compra de una vivienda",
         "Estima el dinero extra que necesitas, además del precio, para comprar una vivienda: impuestos, notaría, registro, gestoría y tasación.",
         """<div class="row"><div><label for="p">Precio de la vivienda (€)</label><input id="p" inputmode="decimal" value="180000"></div><div><label for="t">Impuesto aplicable (%)</label><input id="t" inputmode="decimal" value="8"></div></div>
<div class="row"><div><label for="o1">Notaría, registro y gestoría (% del precio)</label><input id="o1" inputmode="decimal" value="1,5"></div><div><label for="ta">Tasación (€)</label><input id="ta" inputmode="decimal" value="400"></div></div><div id="o"></div>""",
         """function c(){const p=num('p'),imp=p*num('t')/100,not=p*num('o1')/100,ta=num('ta')||0;const tot=imp+not+ta;
$('o').innerHTML=show([['Impuesto',eur(imp)],['Notaría, registro y gestoría',eur(not)],['Tasación',eur(ta)],['Total gastos',eur(tot)],['Gastos sobre el precio',fmt(tot/p*100,1)+' %'],['Si financias el 80%: ahorro necesario',eur(p*0.2+tot)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<h2>¿Qué impuesto pongo?</h2><p>En vivienda de <b>segunda mano</b> se paga el ITP, que fija cada comunidad autónoma (suele estar entre el 6% y el 11%). En <b>obra nueva</b> se paga IVA (10%) más el impuesto de Actos Jurídicos Documentados, también variable por comunidad. Consulta el tipo de tu comunidad. Es una estimación; los importes reales dependen de cada operación.</p>""")

    tool("cuanto-tardo-en-pagar-un-prestamo", "¿Cuánto tardo en pagar una deuda o préstamo? Calculadora de plazo", "¿Cuánto tardo en pagar un préstamo?",
         "Calcula en cuánto tiempo liquidarás una deuda (préstamo, tarjeta, financiación) pagando una cuota fija mensual, y cuántos intereses pagarás.",
         """<div class="row"><div><label for="c">Deuda pendiente (€)</label><input id="c" inputmode="decimal" value="5000"></div><div><label for="i">Interés anual (%)</label><input id="i" inputmode="decimal" value="15"></div></div>
<label for="q">Cuota que pagas al mes (€)</label><input id="q" inputmode="decimal" value="200"><div id="o"></div>""",
         """function c(){const C=num('c'),r=num('i')/100/12,q=num('q');
if(q<=C*r){$('o').innerHTML=show([['Resultado','La cuota no cubre ni los intereses: la deuda no se paga']]);return}
const n=r===0?C/q:-Math.log(1-C*r/q)/Math.log(1+r);
$('o').innerHTML=show([['Tiempo para liquidar',Math.floor(n/12)+' años y '+Math.ceil(n%12)+' meses'],['Número de cuotas',Math.ceil(n)],['Intereses totales',eur(q*n-C)],['Total pagado',eur(q*n)]])}
document.querySelectorAll('input').forEach(i=>i.oninput=c);c();""",
         """<p>Pagar solo el mínimo alarga mucho una deuda con interés alto, como una tarjeta revolving. Subir un poco la cuota mensual puede reducir de forma notable el plazo y los intereses.</p>""")

# Preguntas frecuentes por herramienta (slug -> [(pregunta, respuesta), ...])
FAQS = {
    "calculadora-iva": [
        ("¿Qué tipos de IVA hay en España?", "El tipo general es el 21%, el reducido el 10% y el superreducido el 4%. Algunos productos y servicios básicos tienen tipos reducidos."),
        ("¿Cómo se quita el IVA a un precio?", "Se divide el precio final entre 1,21 si el IVA es del 21%. Por ejemplo, 121 € con IVA son 100 € sin IVA."),
        ("¿Cómo se añade el IVA a un precio?", "Se multiplica el precio sin IVA por 1,21 para el 21%, por 1,10 para el 10% y por 1,04 para el 4%."),
    ],
    "calculadora-hipoteca": [
        ("¿Cómo se calcula la cuota de una hipoteca?", "Con la fórmula de amortización francesa: cuota = capital × i / (1 − (1 + i)^−n), donde i es el interés mensual y n el número de cuotas."),
        ("¿Qué diferencia hay entre hipoteca fija y variable?", "En la fija el interés no cambia durante todo el plazo. En la variable depende del Euríbor más un diferencial y se revisa periódicamente."),
        ("¿Incluye esta calculadora seguros y comisiones?", "No. Calcula solo capital e intereses. Los seguros vinculados y las comisiones aumentan el coste real."),
    ],
    "calculadora-prestamos": [
        ("¿Cómo calculo la cuota de un préstamo personal?", "Introduce el importe, el interés anual (TIN) y el plazo en meses. La calculadora aplica cuota constante con amortización francesa."),
        ("¿Qué es mejor, reducir cuota o plazo?", "Reducir el plazo ahorra más intereses; reducir la cuota alivia tu mes a mes. Depende de tu situación."),
        ("¿Es lo mismo TIN que TAE?", "No. La TAE incluye además las comisiones y es la cifra adecuada para comparar ofertas."),
    ],
    "calcular-letra-dni": [
        ("¿Cómo se calcula la letra del DNI?", "Se divide el número entre 23 y el resto indica la letra en la serie TRWAGMYFPDXBNJZSQVHLCKE."),
        ("¿Sirve para comprobar si un DNI es válido?", "Sí. Si la letra calculada coincide con la del documento, el formato es correcto. No confirma que el DNI exista."),
        ("¿Se guarda el número que escribo?", "No. El cálculo se hace en tu navegador y no se envía a ningún servidor."),
    ],
    "calcular-letra-nie": [
        ("¿Cómo se calcula la letra del NIE?", "Se sustituye la X por 0, la Y por 1 y la Z por 2, se divide el número resultante entre 23 y el resto da la letra."),
        ("¿Cuántas cifras tiene un NIE?", "Empieza por X, Y o Z, sigue con 7 cifras y termina con una letra de control."),
    ],
    "validador-iban": [
        ("¿Cuántos caracteres tiene un IBAN español?", "24: las letras ES, dos dígitos de control y 20 dígitos de la cuenta."),
        ("¿Esta herramienta comprueba que la cuenta existe?", "No. Solo verifica que el IBAN está bien formado y que sus dígitos de control son correctos."),
        ("¿Es seguro escribir mi IBAN aquí?", "El cálculo se hace en tu navegador y no se envía ni guarda. Aun así, no compartas datos bancarios innecesariamente."),
    ],
    "calculadora-imc": [
        ("¿Qué es el IMC?", "El índice de masa corporal relaciona tu peso con tu altura: peso (kg) dividido entre altura (m) al cuadrado."),
        ("¿Qué IMC se considera normal?", "Según la OMS, entre 18,5 y 24,9."),
        ("¿Es fiable el IMC?", "Es solo un indicador general: no distingue entre músculo y grasa. Consulta a un profesional sanitario para valorar tu salud."),
    ],
    "calculadora-interes-compuesto": [
        ("¿Qué es el interés compuesto?", "Es el que se calcula sobre el capital más los intereses ya generados, por lo que el dinero crece cada vez más rápido."),
        ("¿Esta calculadora tiene en cuenta los impuestos?", "No. Tampoco la inflación ni las comisiones. Es una simulación con rentabilidad constante."),
    ],
    "kilometros-a-millas": [
        ("¿Cuántas millas son 10 kilómetros?", "10 km equivalen a unas 6,21 millas."),
        ("¿Cómo paso de km a millas?", "Multiplica los kilómetros por 0,621371, o divídelos entre 1,609344."),
    ],
    "calculadora-porcentajes": [
        ("¿Cómo calculo el 15% de una cantidad?", "Multiplica la cantidad por 15 y divide entre 100. El 15% de 200 es 30."),
        ("¿Cómo calculo una variación porcentual?", "Resta el valor inicial al final, divide entre el inicial y multiplica por 100."),
    ],
    "calculadora-edad": [
        ("¿Cómo se calcula la edad exacta?", "Se restan años, meses y días entre tu fecha de nacimiento y hoy, ajustando por la duración real de cada mes."),
        ("¿Se guarda mi fecha de nacimiento?", "No. Todo se calcula en tu navegador."),
    ],
    "capacidad-endeudamiento-hipoteca": [
        ("¿Qué porcentaje de mis ingresos puedo destinar a la hipoteca?", "Los bancos suelen aceptar entre un 30% y un 35% de tus ingresos netos, contando también otras deudas."),
        ("¿Cuánto financia un banco del precio de la vivienda?", "Habitualmente hasta el 80% del valor de tasación, por lo que necesitas ahorrar el resto y los gastos de compra."),
    ],
    "calculadora-tae": [
        ("¿Para qué sirve la TAE?", "Para comparar el coste real de préstamos distintos, porque incluye intereses, comisiones y la frecuencia de pago."),
        ("¿Por qué la TAE es mayor que el TIN?", "Porque suma el efecto de las comisiones (como la de apertura) y de pagar intereses mensualmente."),
    ],
    "calculadora-indemnizacion-despido": [
        ("¿Cuántos días por año se pagan en un despido improcedente?", "33 días de salario por año trabajado, con un máximo de 24 mensualidades, para contratos posteriores a febrero de 2012."),
        ("¿Y en un despido objetivo?", "20 días de salario por año trabajado, con un máximo de 12 mensualidades."),
        ("¿Esta calculadora es exacta?", "Es orientativa. Si tu contrato es anterior a 2012 se aplican 45 días por año al periodo previo. Consulta a un profesional."),
    ],
    "calculadora-salario-bruto-neto": [
        ("¿Es exacto el sueldo neto que sale?", "No. Es una estimación con una escala media de IRPF y una cotización del 6,5% aprox. Tu nómina real depende de tu comunidad, tu situación familiar y la retención de tu empresa."),
        ("¿Qué diferencia hay entre 12 y 14 pagas?", "El neto anual es el mismo; con 14 pagas cobras dos extras y cada mensualidad es menor."),
    ],
    "calculadora-pagas-extra": [
        ("¿Cobro más con 14 pagas que con 12?", "No. El salario anual es el mismo; solo cambia cómo se reparte entre los meses."),
        ("¿Qué son las pagas prorrateadas?", "Las pagas extra repartidas en las 12 nóminas mensuales, de modo que cobras lo mismo cada mes."),
    ],
    "calculadora-inflacion": [
        ("¿Qué es la inflación?", "Es la subida generalizada y sostenida de los precios, que reduce el poder adquisitivo del dinero con el tiempo."),
        ("¿Cómo se calcula cuánto vale hoy un importe del pasado?", "Se multiplica el importe por (1 + inflación) elevado al número de años. Con una inflación media del 3% anual, 100 € de hoy equivalen a unos 134 € dentro de 10 años."),
        ("¿Usa datos oficiales del IPC?", "No. Aplica la tasa media que tú indiques, por lo que es una estimación."),
    ],
    "calculadora-descuentos": [
        ("¿Cómo se calcula un descuento?", "Precio final = precio original × (1 − descuento/100). Por ejemplo, 80 € con un 25% de descuento son 60 €."),
        ("¿Dos descuentos del 20% y 10% suman un 30%?", "No. Se aplican en cadena: 100 € → 80 € → 72 €, un 28% de descuento total."),
    ],
    "calculadora-roi": [
        ("¿Cómo se calcula el ROI?", "ROI = (ganancia − inversión) / inversión × 100. Invertir 1.000 € y obtener 1.200 € da un ROI del 20%."),
        ("¿Tiene en cuenta el tiempo?", "No. Un 20% en un año no es lo mismo que en cinco; para comparar usa la rentabilidad anualizada."),
    ],
    "calculadora-margen-beneficio": [
        ("¿Qué diferencia hay entre margen y markup?", "El margen se calcula sobre el precio de venta y el markup sobre el coste. Con coste 60 € y venta 100 €, el margen es 40% y el markup 66,7%."),
        ("¿Cómo fijo el precio para un margen concreto?", "Precio = coste / (1 − margen). Para un 30% de margen con coste 70 €, el precio es 100 €."),
    ],
    "calculadora-rentabilidad-alquiler": [
        ("¿Qué es la rentabilidad bruta de un alquiler?", "Es el alquiler anual dividido entre el precio de compra, en porcentaje. No descuenta gastos ni impuestos."),
        ("¿Y la rentabilidad neta?", "Resta gastos como IBI, comunidad, seguros, mantenimiento y periodos vacíos, y es la cifra más realista."),
    ],
    "calculadora-gastos-compra-vivienda": [
        ("¿Qué gastos hay al comprar una vivienda?", "Impuestos (ITP o IVA y AJD según el caso), notaría, registro, gestoría y tasación. Suelen rondar entre el 10% y el 15% del precio."),
        ("¿El resultado es exacto?", "Es orientativo: los impuestos varían según la comunidad autónoma y si la vivienda es nueva o de segunda mano."),
    ],
    "calculadora-ahorro-objetivo": [
        ("¿Cómo sé cuánto ahorrar al mes para una meta?", "Divide el objetivo entre los meses disponibles; si hay rentabilidad, la calculadora ajusta la cuota para tenerla en cuenta."),
        ("¿Incluye impuestos o inflación?", "No. Es una simulación con rentabilidad constante."),
    ],
    "regla-de-tres": [
        ("¿Qué es una regla de tres simple directa?", "Cuando al aumentar una magnitud aumenta la otra en la misma proporción: x = b × c / a."),
        ("¿Y la inversa?", "Cuando al aumentar una magnitud la otra disminuye, como velocidad y tiempo: x = a × b / c."),
    ],
    "dias-entre-fechas": [
        ("¿Se cuenta el día de inicio?", "Por defecto se calcula la diferencia entre ambas fechas, sin incluir el día inicial. Suma 1 si quieres contar ambos extremos."),
        ("¿Cuenta solo días laborables?", "No, cuenta días naturales."),
    ],
    "calculadora-nota-media": [
        ("¿Cómo se calcula la nota media ponderada?", "Se multiplica cada nota por su peso o créditos, se suman los resultados y se divide entre la suma de pesos."),
        ("¿Sirve para la nota de acceso a la universidad?", "Para eso usa la calculadora específica de nota de acceso, que aplica las ponderaciones de la EBAU/PAU."),
    ],
}

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
        ("¿Qué diferencia hay entre interés simple y compuesto?", "En el simple los intereses se calculan siempre sobre el capital inicial. En el compuesto los intereses generados se suman al capital y también producen intereses."),
        ("¿Qué es la regla del 72?", "Dividir 72 entre el tipo de interés anual da, de forma aproximada, los años necesarios para duplicar el capital."),
    ],
    "kilometros-a-millas": [
        ("¿Cuántas millas son 10 kilómetros?", "10 km equivalen a unas 6,21 millas."),
        ("¿Cómo paso de km a millas?", "Multiplica los kilómetros por 0,621371, o divídelos entre 1,609344."),
        ("¿Cuántos kilómetros tiene una milla?", "Una milla equivale a 1,609 km, así que 100 km son unas 62,1 millas."),
    ],
    "calculadora-porcentajes": [
        ("¿Cómo calculo el 15% de una cantidad?", "Multiplica la cantidad por 15 y divide entre 100. El 15% de 200 es 30."),
        ("¿Cómo calculo una variación porcentual?", "Resta el valor inicial al final, divide entre el inicial y multiplica por 100."),
        ("¿Cómo calculo qué porcentaje es una cantidad de otra?", "Divide la parte entre el total y multiplica por 100. Por ejemplo, 30 de 200 es (30 / 200) × 100 = 15%."),
    ],
    "calculadora-edad": [
        ("¿Cómo se calcula la edad exacta?", "Se restan años, meses y días entre tu fecha de nacimiento y hoy, ajustando por la duración real de cada mes."),
        ("¿Se guarda mi fecha de nacimiento?", "No. Todo se calcula en tu navegador."),
        ("¿Cómo se calcula la edad exacta?", "Se restan años, meses y días entre la fecha de nacimiento y la fecha de hoy, ajustando por la longitud de cada mes."),
        ("¿Cuenta los años bisiestos?", "Sí, el cálculo usa el calendario real, así que los 29 de febrero se tienen en cuenta."),
    ],
    "capacidad-endeudamiento-hipoteca": [
        ("¿Qué porcentaje de mis ingresos puedo destinar a la hipoteca?", "Los bancos suelen aceptar entre un 30% y un 35% de tus ingresos netos, contando también otras deudas."),
        ("¿Cuánto financia un banco del precio de la vivienda?", "Habitualmente hasta el 80% del valor de tasación, por lo que necesitas ahorrar el resto y los gastos de compra."),
    ],
    "calculadora-tae": [
        ("¿Para qué sirve la TAE?", "Para comparar el coste real de préstamos distintos, porque incluye intereses, comisiones y la frecuencia de pago."),
        ("¿Por qué la TAE es mayor que el TIN?", "Porque suma el efecto de las comisiones (como la de apertura) y de pagar intereses mensualmente."),
        ("¿Qué diferencia hay entre TIN y TAE?", "El TIN es solo el interés nominal. La TAE incluye además comisiones y la frecuencia de pago, por lo que refleja mejor el coste real."),
        ("¿Qué TAE es buena?", "Cuanto menor, mejor si pides dinero; cuanto mayor, mejor si ahorras. Compara siempre productos con el mismo plazo."),
    ],
    "calculadora-indemnizacion-despido": [
        ("¿Cuántos días por año se pagan en un despido improcedente?", "33 días de salario por año trabajado, con un máximo de 24 mensualidades, para contratos posteriores a febrero de 2012."),
        ("¿Y en un despido objetivo?", "20 días de salario por año trabajado, con un máximo de 12 mensualidades."),
        ("¿Esta calculadora es exacta?", "Es orientativa. Si tu contrato es anterior a 2012 se aplican 45 días por año al periodo previo. Consulta a un profesional."),
    ],
    "calculadora-salario-bruto-neto": [
        ("¿Es exacto el sueldo neto que sale?", "No. Es una estimación con una escala media de IRPF y una cotización del 6,5% aprox. Tu nómina real depende de tu comunidad, tu situación familiar y la retención de tu empresa."),
        ("¿Qué diferencia hay entre 12 y 14 pagas?", "El neto anual es el mismo; con 14 pagas cobras dos extras y cada mensualidad es menor."),
        ("¿Por qué el neto cambia según la comunidad autónoma?", "Porque el tramo autonómico del IRPF es distinto en cada comunidad. Esta calculadora da una estimación; la nómina real depende además de tu situación familiar y contrato."),
        ("¿Qué es la retención de IRPF?", "Es el porcentaje del bruto que la empresa adelanta a Hacienda cada mes. La declaración de la renta ajusta la diferencia final."),
    ],
    "calculadora-pagas-extra": [
        ("¿Cobro más con 14 pagas que con 12?", "No. El salario anual es el mismo; solo cambia cómo se reparte entre los meses."),
        ("¿Qué son las pagas prorrateadas?", "Las pagas extra repartidas en las 12 nóminas mensuales, de modo que cobras lo mismo cada mes."),
        ("¿Cuántas pagas extra suele haber?", "Lo habitual son dos al año (verano y Navidad), pero el convenio puede fijar otras cifras o prorratearlas en 12 mensualidades."),
    ],
    "calculadora-inflacion": [
        ("¿Qué es la inflación?", "Es la subida generalizada y sostenida de los precios, que reduce el poder adquisitivo del dinero con el tiempo."),
        ("¿Cómo se calcula cuánto vale hoy un importe del pasado?", "Se multiplica el importe por (1 + inflación) elevado al número de años. Con una inflación media del 3% anual, 100 € de hoy equivalen a unos 134 € dentro de 10 años."),
        ("¿Usa datos oficiales del IPC?", "No. Aplica la tasa media que tú indiques, por lo que es una estimación."),
    ],
    "calculadora-descuentos": [
        ("¿Cómo se calcula un descuento?", "Precio final = precio original × (1 − descuento/100). Por ejemplo, 80 € con un 25% de descuento son 60 €."),
        ("¿Dos descuentos del 20% y 10% suman un 30%?", "No. Se aplican en cadena: 100 € → 80 € → 72 €, un 28% de descuento total."),
        ("¿Cómo saco el precio original si conozco el precio rebajado?", "Divide el precio final entre (1 − descuento/100). Si algo cuesta 60 € con un 25% de descuento, el original era 60 / 0,75 = 80 €."),
    ],
    "calculadora-roi": [
        ("¿Cómo se calcula el ROI?", "ROI = (ganancia − inversión) / inversión × 100. Invertir 1.000 € y obtener 1.200 € da un ROI del 20%."),
        ("¿Tiene en cuenta el tiempo?", "No. Un 20% en un año no es lo mismo que en cinco; para comparar usa la rentabilidad anualizada."),
        ("¿Qué es un buen ROI?", "Depende del sector y del riesgo. Lo importante es compararlo con alternativas y tener en cuenta el plazo de la inversión."),
        ("¿El ROI tiene en cuenta el tiempo?", "No. Para comparar inversiones de distinta duración conviene calcular también la rentabilidad anualizada."),
    ],
    "calculadora-margen-beneficio": [
        ("¿Qué diferencia hay entre margen y markup?", "El margen se calcula sobre el precio de venta y el markup sobre el coste. Con coste 60 € y venta 100 €, el margen es 40% y el markup 66,7%."),
        ("¿Cómo fijo el precio para un margen concreto?", "Precio = coste / (1 − margen). Para un 30% de margen con coste 70 €, el precio es 100 €."),
        ("¿Qué diferencia hay entre margen y markup?", "El margen es el beneficio sobre el precio de venta; el markup, sobre el coste. Con coste 80 € y venta 100 €, el margen es del 20% y el markup del 25%."),
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
        ("¿Cómo sé si es directa o inversa?", "Pregúntate si al aumentar una magnitud la otra también aumenta (directa) o disminuye (inversa). Más kilos de fruta cuestan más dinero: directa; más obreros tardan menos días: inversa."),
    ],
    "dias-entre-fechas": [
        ("¿Se cuenta el día de inicio?", "Por defecto se calcula la diferencia entre ambas fechas, sin incluir el día inicial. Suma 1 si quieres contar ambos extremos."),
        ("¿Cuenta solo días laborables?", "No, cuenta días naturales."),
        ("¿Se cuenta el día de inicio?", "Por defecto se calcula la diferencia entre ambas fechas, sin incluir el día inicial. Si necesitas contarlo, suma un día al resultado."),
    ],
    "calculadora-nota-media": [
        ("¿Cómo se calcula la nota media ponderada?", "Se multiplica cada nota por su peso o créditos, se suman los resultados y se divide entre la suma de pesos."),
        ("¿Sirve para la nota de acceso a la universidad?", "Para eso usa la calculadora específica de nota de acceso, que aplica las ponderaciones de la EBAU/PAU."),
        ("¿Qué pasa si todas las asignaturas pesan lo mismo?", "Deja el mismo peso en todas y el resultado será la media aritmética: suma las notas y divide entre el número de asignaturas."),
    ],
    "calculadora-propinas": [
        ("¿Cuánta propina se suele dejar en España?", "No es obligatoria. Es habitual dejar entre un 5% y un 10% si el servicio ha sido bueno, y muchos lo redondean al euro más cercano."),
        ("¿Cómo divido la cuenta entre varias personas?", "Indica el número de comensales y la calculadora reparte el total con propina incluida a partes iguales."),
        ("¿Puedo redondear la propina?", "Sí. Muchas personas redondean el total al euro o a los 5 € más cercanos para simplificar el pago; ajusta el porcentaje hasta obtener la cifra que prefieras."),
    ],
    "calculadora-pitagoras": [
        ("¿Qué dice el teorema de Pitágoras?", "En un triángulo rectángulo, la suma de los cuadrados de los catetos es igual al cuadrado de la hipotenusa: a² + b² = c²."),
        ("¿Puedo calcular un cateto si conozco la hipotenusa?", "Sí. Se resuelve restando: a = √(c² − b²)."),
        ("¿Cuándo se puede usar el teorema de Pitágoras?", "Solo en triángulos rectángulos: el cuadrado de la hipotenusa es la suma de los cuadrados de los catetos."),
    ],
    "calculadora-fracciones": [
        ("¿Cómo se suman fracciones con distinto denominador?", "Se busca un denominador común, se convierten las fracciones y se suman los numeradores. Después se simplifica el resultado."),
        ("¿Cómo se simplifica una fracción?", "Se dividen numerador y denominador entre su máximo común divisor."),
    ],
    "celsius-a-fahrenheit": [
        ("¿Cuál es la fórmula de Celsius a Fahrenheit?", "°F = °C × 9/5 + 32. Por ejemplo, 20 °C equivalen a 68 °F."),
        ("¿Y de Fahrenheit a Celsius?", "°C = (°F − 32) × 5/9."),
        ("¿Cuál es la fórmula para pasar de Celsius a Fahrenheit?", "Se multiplica por 1,8 y se suman 32: °F = °C × 1,8 + 32. Por ejemplo, 20 °C son 68 °F."),
    ],
    "kilos-a-libras": [
        ("¿Cuántas libras son un kilo?", "Un kilogramo equivale a unas 2,2046 libras."),
        ("¿Cómo paso libras a kilos?", "Se multiplica por 0,4536 o se divide entre 2,2046."),
        ("¿Cuántas libras es un kilo?", "Un kilo equivale a unas 2,2046 libras. Para pasar de libras a kilos se multiplica por 0,4536."),
    ],
    "kmh-a-mph": [
        ("¿Cuántas millas por hora son 100 km/h?", "Unas 62,14 mph. Un km/h equivale a 0,6214 mph."),
        ("¿Cómo paso mph a km/h?", "Se multiplica por 1,609."),
        ("¿Cuántas mph son 120 km/h?", "Unas 74,6 mph. Como regla rápida, multiplica los km/h por 0,62."),
    ],
    "numeros-romanos": [
        ("¿Qué valor tiene cada símbolo romano?", "I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 y M = 1000."),
        ("¿Hasta qué número se puede convertir?", "Con la notación estándar, hasta 3999 (MMMCMXCIX)."),
    ],
    "generador-contrasenas": [
        ("¿Qué hace segura una contraseña?", "La longitud sobre todo: se recomiendan 14 caracteres o más, mezclando letras, números y símbolos, y una distinta para cada servicio."),
        ("¿Se guarda la contraseña generada?", "No. Se genera en tu navegador y no se envía a ningún servidor."),
    ],
    "amortizacion-anticipada-hipoteca": [
        ("¿Qué es amortizar anticipadamente una hipoteca?", "Es adelantar dinero al banco para reducir la deuda pendiente antes de lo previsto, ya sea acortando el plazo o bajando la cuota."),
        ("¿Es mejor reducir plazo o cuota?", "Reducir el plazo suele ahorrar más intereses en total; reducir la cuota da más holgura mensual. Depende de tu situación."),
        ("¿Hay comisión por amortización anticipada?", "Puede haberla según el contrato y la fecha de firma. Consulta tu escritura o pregunta a tu banco."),
    ],
    "calculadora-area-figuras": [
        ("¿Cómo se calcula el área de un círculo?", "Con la fórmula π × radio². Si conoces el diámetro, divídelo entre 2 para obtener el radio."),
        ("¿Y el área de un triángulo?", "Base × altura / 2."),
        ("¿En qué unidades sale el resultado?", "En las mismas unidades que introduzcas, elevadas al cuadrado: si usas metros, el área sale en m²."),
    ],
    "calculadora-media-mediana-moda": [
        ("¿Qué diferencia hay entre media, mediana y moda?", "La media es el promedio de todos los valores, la mediana es el valor central al ordenarlos y la moda es el que más se repite."),
        ("¿Cuándo es mejor usar la mediana?", "Cuando hay valores extremos que distorsionan la media, por ejemplo en salarios o precios de vivienda."),
    ],
    "centimetros-a-pulgadas": [
        ("¿Cuántas pulgadas son 10 centímetros?", "Unas 3,94 pulgadas. Una pulgada equivale exactamente a 2,54 cm."),
        ("¿Cómo paso pulgadas a centímetros?", "Multiplica las pulgadas por 2,54."),
        ("¿Cuántos centímetros tiene una pulgada?", "Una pulgada son exactamente 2,54 cm."),
    ],
    "litros-a-galones": [
        ("¿Cuántos galones son 10 litros?", "Unos 2,64 galones estadounidenses. Un galón US son 3,785 litros."),
        ("¿El galón de EE. UU. y el británico son iguales?", "No. El galón imperial británico equivale a unos 4,546 litros, más grande que el estadounidense."),
        ("¿Un galón es siempre igual?", "No. El galón estadounidense son 3,785 litros y el imperial (Reino Unido) 4,546 litros."),
    ],
    "conversor-binario-decimal-hexadecimal": [
        ("¿Cómo se pasa de binario a decimal?", "Cada dígito binario vale una potencia de 2 según su posición, de derecha a izquierda; se suman las de los dígitos que son 1."),
        ("¿Qué es el sistema hexadecimal?", "Es un sistema en base 16 que usa los dígitos 0-9 y las letras A-F. Se usa mucho en informática, por ejemplo en los colores web."),
    ],
    "dias-para-navidad": [
        ("¿Qué día se cuenta como Navidad?", "El 25 de diciembre."),
        ("¿Se actualiza solo el número de días?", "Sí. Se calcula en tu navegador con la fecha de hoy cada vez que abres la página."),
    ],
    "numero-de-semana": [
        ("¿Qué es el número de semana ISO?", "Es la numeración estándar ISO 8601: las semanas empiezan en lunes y la semana 1 es la que contiene el primer jueves del año."),
        ("¿Cuántas semanas tiene un año?", "52 o 53, según el año."),
    ],
    "calculadora-horas-trabajadas": [
        ("¿Cómo se calculan las horas trabajadas?", "Se resta la hora de entrada a la de salida y se descuentan los descansos no remunerados."),
        ("¿Sirve para turnos que cruzan la medianoche?", "Sí, siempre que indiques correctamente las horas de entrada y salida."),
    ],
    "calculadora-nota-acceso-universidad": [
        ("¿Cómo se calcula la nota de acceso?", "Se combina la nota media del bachillerato y la de la fase general de la prueba de acceso, con la ponderación que establece la normativa vigente."),
        ("¿Es una cifra oficial?", "No, es una estimación orientativa. La nota oficial la publica tu universidad o comunidad autónoma."),
    ],
    "calculadora-pintura": [
        ("¿Cuánta pintura necesito para una habitación?", "Calcula la superficie de paredes (y techo si procede) y divídela entre el rendimiento por litro indicado en el bote, normalmente 8-12 m²/l."),
        ("¿Cuántas manos conviene dar?", "Lo habitual son dos manos, por lo que conviene multiplicar la cantidad por dos."),
        ("¿Se descuentan puertas y ventanas?", "Para un cálculo más ajustado, resta su superficie de la total."),
    ],
    "contador-caracteres-redes": [
        ("¿Cuántos caracteres admite cada red social?", "Varía según la plataforma y cambia con el tiempo. Comprueba el límite vigente en la propia red antes de publicar."),
        ("¿Cuentan los espacios y los emojis?", "Los espacios cuentan como caracteres. Los emojis pueden contar como más de uno según la plataforma."),
    ],
    "contador-palabras": [
        ("¿Cómo cuenta las palabras?", "Separa el texto por espacios y saltos de línea."),
        ("¿Se guarda mi texto?", "No. El recuento se hace en tu navegador y el texto no se envía a ningún servidor."),
    ],
    "conversor-unidades": [
        ("¿Qué unidades puedo convertir?", "Las de longitud, peso, volumen y otras magnitudes habituales que ofrece la herramienta."),
        ("¿Es exacto el resultado?", "Usa factores de conversión estándar y redondea el resultado para facilitar la lectura."),
    ],
    "conversor-zonas-horarias": [
        ("¿Tiene en cuenta el cambio de hora de verano?", "Sí, el cálculo usa las reglas de zonas horarias de tu navegador, que incluyen el horario de verano."),
        ("¿Qué diferencia hay entre España peninsular y Canarias?", "Canarias va una hora por detrás de la península durante todo el año."),
    ],
    "convertidor-mayusculas": [
        ("¿Qué formatos admite?", "Convierte el texto a MAYÚSCULAS, minúsculas y otros estilos de capitalización."),
        ("¿Se guarda mi texto?", "No. La conversión se hace en tu navegador."),
    ],
    "coste-viaje-gasolina": [
        ("¿Cómo se calcula el coste de un viaje en coche?", "Se multiplican los kilómetros por el consumo (l/100 km) dividido entre 100 y por el precio del litro."),
        ("¿Incluye peajes o desgaste?", "No. Solo calcula el combustible; los peajes, aparcamiento y mantenimiento se suman aparte."),
    ],
    "cuanto-tardo-en-pagar-un-prestamo": [
        ("¿Cómo se calcula el tiempo para pagar un préstamo?", "A partir del capital, el interés y la cuota que puedes pagar al mes se obtiene el número de cuotas necesarias."),
        ("¿Qué pasa si la cuota es menor que los intereses?", "La deuda no se amortiza nunca: necesitas una cuota mayor que los intereses mensuales."),
        ("¿Cómo acorto el plazo de un préstamo?", "Con amortizaciones anticipadas o aumentando la cuota. Cuanto antes se hagan, más intereses se ahorran."),
    ],
    "lanzar-dado-moneda": [
        ("¿Son aleatorios los lanzamientos?", "Usan números pseudoaleatorios del navegador, suficientes para juegos y decisiones cotidianas."),
        ("¿Qué probabilidad tiene cada resultado?", "En una moneda, 50 % cada cara; en un dado de seis caras, un 16,7 % cada número."),
    ],
    "numero-aleatorio": [
        ("¿Puedo elegir el rango?", "Sí, indica el mínimo y el máximo y se generará un número entre ambos."),
        ("¿Sirve para sorteos oficiales o criptografía?", "No. Es aleatoriedad pensada para uso cotidiano."),
        ("¿Los números son realmente aleatorios?", "Son pseudoaleatorios, generados por el navegador. Valen para sorteos y juegos, pero no para criptografía."),
    ],
    "revision-hipoteca-variable-euribor": [
        ("¿Cómo afecta el Euríbor a mi cuota?", "En una hipoteca variable el interés es el Euríbor más un diferencial; si el Euríbor sube o baja en la revisión, tu cuota cambia."),
        ("¿Cada cuánto se revisa?", "Lo habitual es cada 6 o 12 meses, según indique tu contrato."),
        ("¿Es el resultado definitivo?", "No, es una simulación. La cuota real la fija tu banco."),
    ],
    "sorteo-aleatorio": [
        ("¿Cómo funciona el sorteo?", "Elige al azar entre los nombres o elementos que introduzcas."),
        ("¿Es válido para sorteos con premios?", "Para sorteos públicos o con premios conviene seguir la normativa aplicable y las bases del sorteo."),
    ],
    "sumar-dias-a-fecha": [
        ("¿Cómo sumo o resto días a una fecha?", "Indica la fecha de partida y el número de días; usa un valor negativo para restar."),
        ("¿Cuenta los días laborables?", "No, cuenta días naturales."),
    ],
    "calculadora-calorias-tmb": [
        ("¿Qué es el metabolismo basal?", "Son las calorías que tu cuerpo gasta en reposo para mantener funciones vitales como respirar o la circulación."),
        ("¿Es exacto el resultado?", "Es una estimación con la ecuación de Mifflin-St Jeor. El gasto real varía de una persona a otra."),
        ("¿Qué es la tasa metabólica basal?", "Son las calorías que tu cuerpo gasta en reposo para mantener sus funciones vitales. Se multiplica por un factor de actividad para estimar el gasto diario total."),
    ],
    "calculadora-peso-ideal": [
        ("¿Existe un único peso ideal?", "No. Se habla de un rango saludable, que depende de la altura, la constitución y la masa muscular."),
        ("¿Qué IMC se considera normal?", "Según la OMS, entre 18,5 y 24,9."),
        ("¿Existe un único peso ideal?", "No. Las fórmulas dan un rango orientativo; la constitución, la edad y la masa muscular influyen. Consulta a un profesional sanitario."),
    ],
    "calculadora-ritmo-carrera": [
        ("¿Qué es el ritmo en carrera?", "Es el tiempo que tardas en recorrer un kilómetro, expresado en minutos por kilómetro."),
        ("¿Cómo paso de min/km a km/h?", "Divide 60 entre el ritmo en minutos. Por ejemplo, 5:00 min/km son 12 km/h."),
        ("¿Cómo se calcula el ritmo por kilómetro?", "Dividiendo el tiempo total entre los kilómetros recorridos. Por ejemplo, 50 minutos en 10 km son 5:00 min/km."),
    ],
    "calculadora-fecha-probable-parto": [
        ("¿Cómo se calcula la fecha probable de parto?", "Se suman 280 días (40 semanas) al primer día de la última regla, con la regla de Naegele."),
        ("¿Es una fecha segura?", "No, es una estimación. Tu médico o matrona la ajustará con la ecografía."),
    ],
    "calculadora-vacaciones": [
        ("¿Cuántas vacaciones me corresponden por ley en España?", "Un mínimo de 30 días naturales al año, que tu convenio o contrato pueden mejorar."),
        ("¿Y si no trabajo el año completo?", "Se calculan en proporción al tiempo trabajado."),
        ("¿Las vacaciones se pagan o se disfrutan?", "Deben disfrutarse. Solo se compensan en dinero si el contrato termina con días pendientes de disfrutar."),
    ],
    "calculadora-consumo-electrico": [
        ("¿Cómo se calcula el coste de un electrodoméstico?", "Potencia en kW por horas de uso da los kWh consumidos, que se multiplican por el precio del kWh."),
        ("¿Dónde veo la potencia del aparato?", "En la etiqueta del producto o en su manual, expresada en vatios (W)."),
        ("¿Cómo reduzco el consumo de mis aparatos?", "Apaga el modo en espera, elige aparatos con etiqueta energética A o B y usa los programas eco. El consumo en espera puede suponer una parte apreciable de la factura."),
    ],
    "calculadora-consumo-combustible": [
        ("¿Cómo calculo el consumo real de mi coche?", "Llena el depósito, anota los kilómetros, circula y vuelve a llenarlo: litros repostados entre kilómetros por 100."),
        ("¿Por qué difiere del consumo oficial?", "El oficial se mide en condiciones de laboratorio; el real depende de la conducción, la carga y el tráfico."),
        ("¿Cómo puedo reducir el consumo de mi coche?", "Mantén la presión de los neumáticos correcta, evita acelerones y frenazos, no lleves peso innecesario y usa marchas largas a velocidad constante."),
    ],
    "calculadora-ecuacion-segundo-grado": [
        ("¿Qué es el discriminante?", "Es b² − 4ac. Si es positivo hay dos soluciones reales, si es cero una doble y si es negativo ninguna real."),
        ("¿Qué pasa si a vale 0?", "Deja de ser de segundo grado: es una ecuación lineal."),
        ("¿Cuál es la fórmula para resolverla?", "x = (−b ± √(b² − 4ac)) / 2a. El signo ± da las dos soluciones posibles."),
    ],
}

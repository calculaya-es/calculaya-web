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
}

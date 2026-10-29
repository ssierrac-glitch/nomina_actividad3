# Informe de desarrollo — Sistema de nómina

## 1. Objetivo

Diseñar un sistema de nómina que use programación orientada a objetos para liquidar empleados asalariados, por horas, por comisión y temporales. El sistema calcula el salario bruto, las deducciones obligatorias, el depósito voluntario de ahorro y el salario neto, y distingue los beneficios que asume la empresa.

## 2. Reglas de negocio implementadas

| Tipo | Cálculo del bruto | Beneficios |
|---|---|---|
| Asalariado | Salario mensual fijo más el bono del 10% cuando la antigüedad es mayor a cinco años | Alimentación por $1.000.000 a cargo de la empresa |
| Por horas | Hasta 40 horas a tarifa normal; las horas que exceden 40 a 1,5 veces la tarifa | Sin bono. Ahorro de 2% del bruto con más de un año y aceptación del empleado |
| Por comisión | Salario base más porcentaje configurado sobre las ventas y, si las ventas superan $20.000.000, bono del 3% de las ventas | Alimentación por $1.000.000 a cargo de la empresa |
| Temporal | Salario mensual fijo y duración positiva del contrato | Sin bonos ni beneficios adicionales |

A todos se les aplica seguridad social y pensión del 4% sobre el bruto. La tasa ARL se deja configurable porque el enunciado no especifica su valor. El neto es bruto menos seguridad social/pensión, ARL y ahorro, si aplica. El beneficio de alimentación no se resta al empleado ni se añade al neto: se informa como costo/beneficio de la empresa.

## 3. Diseño orientado a objetos

- `SalariedEmployee`, `HourlyEmployee`, `CommissionEmployee` y `TemporaryEmployee` modelan las variantes del dominio y son objetos inmutables.
- El contrato `Employee` establece lo que el servicio necesita: identificador, nombre, bruto, beneficio de alimentación y depósito de ahorro.
- `PayrollService` recibe cualquier objeto que cumpla ese contrato. Calcula las deducciones y construye un `PayrollResult` inmutable.
- `PayrollResult` contiene los importes ya redondeados a centavos, lo que evita mezclar el cálculo con su presentación.
- `nomina.__main__` crea datos de demostración y los presenta en consola; la lógica de negocio permanece en los modelos y el servicio.

## 4. SOLID y buenas prácticas

- **S — Responsabilidad única:** cada clase de empleado calcula su remuneración; el servicio aplica deducciones; el resultado solo transporta datos.
- **O — Abierto/cerrado:** puede incorporarse otro tipo que cumpla `Employee` sin cambiar las fórmulas del servicio.
- **L — Sustitución de Liskov:** las cuatro variantes cumplen las operaciones que espera el contrato y se pueden entregar al servicio de la misma manera.
- **I — Segregación de interfaces:** el contrato expone únicamente los datos y cálculos que necesita liquidación.
- **D — Inversión de dependencias:** la liquidación depende del contrato `Employee`, no inspecciona las clases concretas.
- Los nombres de clases y métodos reflejan el dominio; los modelos son inmutables; `Decimal` evita errores de precisión monetaria; las tasas incompletas se configuran y documentan.

## 5. Validaciones

- Identificador y nombre no vacíos.
- Salarios, tarifa por hora, horas trabajadas, ventas y antigüedad no negativos.
- Porcentaje de comisión y tasas de deducción entre 0 y 1.
- Duración del contrato temporal mayor que cero.
- Ahorro sujeto a antigüedad mayor de un año y aceptación.
- Rechazo de toda liquidación cuyo neto sea negativo.

## 6. Pruebas unitarias

`tests/test_payroll.py` usa `unittest`, incluido en Python, y prueba:

1. Bono de antigüedad exactamente a los cinco años y después de cumplir cinco.
2. Horas extra a 1,5 veces la tarifa.
3. Elegibilidad y consentimiento para el ahorro.
4. Comisión, bono de ventas y umbral exacto de $20.000.000.
5. Ausencia de beneficios para el empleado temporal.
6. Rechazo de horas, ventas o salarios negativos y contrato inválido.
7. Rechazo de salario neto negativo.

Comando para ejecutarlas: `python -m unittest discover -s tests -v` con `PYTHONPATH=src`.

## 7. Metodología de desarrollo

Se propone un proceso iterativo e incremental con prácticas de Programación Extrema (XP):

1. **Historias y criterios de aceptación:** redactar reglas comprobables, por ejemplo, «como empleado por horas, quiero que cada hora después de la 40 se pague al 150%».
2. **Diseño simple del dominio:** definir modelos de empleados, contrato común, servicio de liquidación y resultado.
3. **Desarrollo en incrementos pequeños:** implementar una regla a la vez y revisar sus límites.
4. **Pruebas unitarias:** comprobar valores esperados y casos no válidos; ejecutar la suite después de cambios.
5. **Refactorización:** simplificar estructura y eliminar duplicación preservando el comportamiento demostrado por las pruebas.
6. **Integración y revisión por pares:** cada integrante presenta su cambio al CIPA y otro integrante revisa reglas, pruebas y claridad.
7. **Control de versiones:** commits pequeños y descriptivos por integrante, ramas para cambios y fusión revisada a la rama principal.
8. **Entrega continua:** ejecutar la demostración y pruebas, actualizar la documentación y preparar la grabación.

## 8. Uso y demostración

Desde la carpeta raíz del proyecto, configure `PYTHONPATH=src` y ejecute `python -m nomina`. La salida presenta los cuatro empleados de ejemplo. Para validar cambios, ejecute `python -m unittest discover -s tests -v`.

## 9. Pendientes del CIPA antes de la publicación

- Confirmar con el docente la tasa de ARL y cómo espera presentar su responsable contable; el enunciado la llama deducción, aunque no fija tasa.
- Acordar la tasa de comisión para los casos de demostración, ya que no aparece en el enunciado.
- Reemplazar los nombres/roles del guion por integrantes y aportes reales.
- Crear o indicar el repositorio remoto GitHub del CIPA y publicar allí el código con el historial verdadero.
- Grabar, revisar y publicar el video en el canal de YouTube definido por el equipo.

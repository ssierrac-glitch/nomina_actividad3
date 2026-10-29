# Guion para el video de exposición del CIPA

**Duración sugerida:** 6–8 minutos. Sustituyan los campos entre corchetes por información real del equipo.

## 1. Presentación — 30 segundos

**[Integrante 1]:** «Hola, somos el CIPA [nombre o número]. En esta actividad presentamos un sistema de nómina desarrollado en Python con programación orientada a objetos. El sistema liquida cuatro tipos de empleados y valida las reglas indicadas en la actividad».

## 2. Reglas del problema — 1 minuto

**[Integrante 1]:** «Los empleados asalariados tienen salario fijo y pueden recibir un bono del 10% después de más de cinco años. Los empleados por horas reciben tarifa normal hasta 40 horas y recargo de 1,5 veces por las horas adicionales. Los empleados por comisión reciben salario base y comisión sobre ventas, con un bono del 3% si superan veinte millones. Los temporales reciben salario fijo y no tienen beneficios adicionales».

«El sistema también calcula el 4% de seguridad social y pensión, el ahorro voluntario elegible para empleados por horas y el beneficio de alimentación cubierto por la empresa para asalariados y empleados por comisión».

## 3. Diseño del sistema — 1,5 minutos

**[Integrante 2, compartir `src/nomina/employees/base.py`]:** «Cada tipo de empleado mantiene su propia regla de cálculo. Todos cumplen un contrato común que informa salario bruto, alimentación y ahorro. Así el servicio no necesita preguntar qué clase concreta está procesando».

**[Integrante 2, compartir `src/nomina/payroll.py`]:** «`PayrollService` aplica las deducciones y genera un resultado. Separar estas responsabilidades facilita agregar otro tipo de empleado y mantener el cálculo». Explicar brevemente responsabilidad única, extensión mediante el contrato y uso de `Decimal` para dinero.

## 4. Demostración — 1,5 minutos

**[Integrante 3, compartir consola]:** «Ejecutamos `python -m nomina`. La demostración calcula un empleado de cada tipo. Revisemos el bruto, las deducciones, el ahorro, el neto y la alimentación que asume la empresa».

Explicar el caso de horas extra y el caso de comisión. Aclarar que el porcentaje de comisión y la tasa ARL son configurables porque el enunciado no define esos valores. La demostración usa 4% de comisión y 1% de ARL como datos ilustrativos, no como reglas oficiales.

## 5. Pruebas y validaciones — 1 minuto

**[Integrante 3]:** «Ejecutamos `python -m unittest discover -s tests -v`. Las pruebas revisan los umbrales de antigüedad y ventas, horas extra, ahorro con consentimiento, beneficios de los temporales y rechazo de datos inválidos. La aplicación impide horas, ventas y salarios negativos, y no permite una liquidación con neto negativo».

## 6. Metodología y GitHub — 1 minuto

**[Integrante 4]:** «Organizamos el desarrollo en incrementos: analizamos reglas, diseñamos el dominio, implementamos cálculos, verificamos con pruebas y refactorizamos conservando el comportamiento. Usamos prácticas iterativas inspiradas en XP y revisión por pares».

Compartir el repositorio real del CIPA: mostrar commits de cada integrante, cambios por etapas y rama principal. No mostrar historial de ejemplo como si fuera actividad ya realizada.

## 7. Cierre — 20 segundos

**[Integrante 1]:** «Con esto demostramos cómo aplicar orientación a objetos, principios SOLID, validaciones, pruebas unitarias y control de versiones a un problema de nómina. Gracias por su atención».

## Lista de verificación antes de publicar

- Confirmar la tasa ARL y la tasa de comisión con el docente.
- Cambiar nombres y roles por integrantes reales; dar oportunidad de participación a cada miembro del CIPA.
- Ejecutar la demostración y la suite de pruebas en la grabación.
- Mostrar el repositorio GitHub real y su historial de commits.
- Verificar audio, legibilidad de pantalla y permisos del enlace de YouTube antes de compartirlo con el docente.

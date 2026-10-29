# Actividad 3 — Sistema de nómina orientado a objetos

 Proyecto académico en Python que calcula la nómina mensual de cuatro tipos de empleados, sus deducciones y beneficios asociados.

## Contenido del proyecto

```text
actividad3_nomina/
├── src/nomina/
│   ├── employees/base.py  # contrato común y cuatro tipos de empleado
│   ├── models.py          # resultado inmutable de la liquidación
│   ├── payroll.py         # servicio común de nómina
│   └── __main__.py        # demostración ejecutable
├── tests/test_payroll.py  # pruebas unitarias
├── docs/
│   ├── informe.md         # explicación de diseño, reglas y metodología

├── deliverables/
│   └── actividad3_sistema_nomina.pptx  # ```

## Requisitos

- Python 3.10 o superior.
- No requiere dependencias externas.

## Ejecutar la demostración

Desde la raíz de esta carpeta, en PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m nomina
```

La demostración crea un empleado de cada tipo y muestra bruto, deducciones, ahorro, neto y alimentación cubierta por la empresa.

## Ejecutar las pruebas

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Las pruebas cubren umbrales, recargos, beneficios, deducciones y datos inválidos.

## Decisiones y supuestos

1. **Seguridad social y pensión:** el enunciado da una tasa total de 4%; se calcula como una única deducción del bruto.
2. **ARL:** se tomo un ejemplo de 1% indica tasa. 
3. **Comisión:** el porcentaje no se especifica. Se proporciona al crear cada empleado por comisión.
4. **Salario bruto:** incluye salario base, horas extra, comisiones y bonos en efectivo; el 4% y la ARL se calculan sobre este total.
5. **Alimentación:** se muestra separada como beneficio a cargo de la empresa y no se suma al neto que recibe el empleado.
6. **Ahorro:** para el empleado por horas elegible que acepta, se calcula el 2% del bruto y se reporta como depósito/deducción separada del neto.
7. **Umbrales estrictos:** los bonos aplican al superar 5 años y al superar $20.000.000 en ventas; exactamente el umbral no activa el bono.
8. **Moneda:** los importes se reciben como `Decimal` y se redondean a dos decimales para evitar errores binarios de punto flotante.


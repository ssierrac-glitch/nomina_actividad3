# Actividad 3 — Sistema de nómina orientado a objetos

**Entrega CIPA.** Proyecto académico en Python que calcula la nómina mensual de cuatro tipos de empleados, sus deducciones y beneficios asociados.

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
│   └── guion_video.md     # guion para exponer en CIPA
├── deliverables/
│   └── actividad3_sistema_nomina.pptx  # presentación de apoyo para el video
└── README.md
```

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
2. **ARL:** el enunciado no indica tasa. Se configura al crear `PayrollService`; su valor predeterminado es 0. En la demostración se usa 1% solo para visualizar la operación. El CIPA debe confirmar la tasa requerida por el docente antes de entregar cálculos como definitivos.
3. **Comisión:** el porcentaje no se especifica. Se proporciona al crear cada empleado por comisión.
4. **Salario bruto:** incluye salario base, horas extra, comisiones y bonos en efectivo; el 4% y la ARL se calculan sobre este total.
5. **Alimentación:** se muestra separada como beneficio a cargo de la empresa y no se suma al neto que recibe el empleado.
6. **Ahorro:** para el empleado por horas elegible que acepta, se calcula el 2% del bruto y se reporta como depósito/deducción separada del neto.
7. **Umbrales estrictos:** los bonos aplican al superar 5 años y al superar $20.000.000 en ventas; exactamente el umbral no activa el bono.
8. **Moneda:** los importes se reciben como `Decimal` y se redondean a dos decimales para evitar errores binarios de punto flotante.

## GitHub y control de versiones del CIPA

El código y la documentación están preparados para publicarse. Para evidenciar el trabajo colaborativo, cada integrante debe usar su propia cuenta GitHub y dejar commits identificables; no se deben inventar autores ni historial. Desde la raíz del proyecto, creen el remoto del equipo y sigan las instrucciones del repositorio para subir la rama principal. El repositorio remoto y la lista de integrantes aún deben ser definidos por el CIPA.

Para una secuencia clara de commits, pueden registrar por separado: estructura y modelos; reglas de liquidación; pruebas y validaciones; documentación y guion. En el video, muestren el historial real del repositorio.

## Presentación

El informe y el guion están en `docs/`. Personalicen el guion con nombres y aportes reales del CIPA antes de grabar y publicar el video en YouTube.

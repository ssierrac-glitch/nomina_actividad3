"""Demostración ejecutable: python -m nomina"""

from decimal import Decimal as D

from nomina.employees import CommissionEmployee, HourlyEmployee, SalariedEmployee, TemporaryEmployee
from nomina.payroll import PayrollService


def main() -> None:
    employees = [
        SalariedEmployee("E001", "Laura Gómez", D("3500000"), 7),
        HourlyEmployee("E002", "Carlos Ruiz", D("15000"), D("45"), 2, True),
        CommissionEmployee("E003", "Diana Mora", D("1800000"), D("25000000"), D("0.04")),
        TemporaryEmployee("E004", "Andrés Gil", D("2200000"), 6),
    ]
    payroll = PayrollService(arl_rate=D("0.01"))
    print("LIQUIDACIÓN DE NÓMINA (valores en COP)")
    print("Empleado                 Bruto          SS/Pensión       ARL       Ahorro          Neto   Alimentación")
    for result in payroll.calculate_many(employees):
        print(
            f"{result.employee_name:<23} {result.gross_salary:>12,.2f}"
            f" {result.social_pension_deduction:>15,.2f} {result.arl_deduction:>10,.2f}"
            f" {result.savings_deposit:>11,.2f} {result.net_salary:>14,.2f}"
            f" {result.employer_food_benefit:>13,.2f}"
        )


if __name__ == "__main__":
    main()

"""Servicio que combina remuneración y deducciones sin conocer clases concretas."""

from decimal import Decimal, ROUND_HALF_UP

from nomina.employees.base import Employee
from nomina.models import PayrollResult

CENT = Decimal("0.01")
ZERO = Decimal("0")


def money(value: Decimal) -> Decimal:
    """Redondea el importe monetario al centavo más cercano."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


class PayrollService:
    """Calcula una nómina aplicando las tasas de deducción configuradas."""

    def __init__(self, social_pension_rate: Decimal = Decimal("0.04"), arl_rate: Decimal = ZERO) -> None:
        for label, rate in (("seguridad social y pensión", social_pension_rate), ("ARL", arl_rate)):
            if not ZERO <= rate <= Decimal("1"):
                raise ValueError(f"La tasa de {label} debe estar entre 0 y 1.")
        self.social_pension_rate = social_pension_rate
        self.arl_rate = arl_rate

    def calculate(self, employee: Employee) -> PayrollResult:
        gross = employee.gross_salary()
        social_pension = gross * self.social_pension_rate
        arl = gross * self.arl_rate
        savings = employee.savings_deposit()
        net = gross - social_pension - arl - savings
        if net < ZERO:
            raise ValueError("El salario neto no puede ser negativo.")

        return PayrollResult(
            employee_id=employee.employee_id,
            employee_name=employee.name,
            gross_salary=money(gross),
            social_pension_deduction=money(social_pension),
            arl_deduction=money(arl),
            savings_deposit=money(savings),
            net_salary=money(net),
            employer_food_benefit=money(employee.employer_food_benefit()),
        )

    def calculate_many(self, employees: list[Employee]) -> list[PayrollResult]:
        """Liquida una lista en el mismo orden en que fue recibida."""
        return [self.calculate(employee) for employee in employees]

"""Entidades del dominio y reglas de remuneración por tipo de empleado."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol

from nomina.models import Money

ZERO = Decimal("0")


class Employee(Protocol):
    """Contrato que consume el servicio de nómina."""

    employee_id: str
    name: str

    def gross_salary(self) -> Money: ...

    def employer_food_benefit(self) -> Money: ...

    def savings_deposit(self) -> Money: ...


def validate_identity(employee_id: str, name: str) -> None:
    if not employee_id.strip() or not name.strip():
        raise ValueError("El identificador y el nombre son obligatorios.")


@dataclass(frozen=True)
class SalariedEmployee:
    employee_id: str
    name: str
    monthly_salary: Money
    years_of_service: int

    def __post_init__(self) -> None:
        validate_identity(self.employee_id, self.name)
        if self.monthly_salary < ZERO or self.years_of_service < 0:
            raise ValueError("El salario y la antigüedad no pueden ser negativos.")

    def gross_salary(self) -> Money:
        # El bono en efectivo forma parte del bruto sujeto a deducciones.
        bonus = self.monthly_salary * Decimal("0.10") if self.years_of_service > 5 else ZERO
        return self.monthly_salary + bonus

    def employer_food_benefit(self) -> Money:
        return Decimal("1000000")

    def savings_deposit(self) -> Money:
        return ZERO


@dataclass(frozen=True)
class HourlyEmployee:
    employee_id: str
    name: str
    hourly_rate: Money
    hours_worked: Money
    years_of_service: int = 0
    accepts_savings_fund: bool = False

    def __post_init__(self) -> None:
        validate_identity(self.employee_id, self.name)
        if self.hourly_rate < ZERO or self.hours_worked < ZERO or self.years_of_service < 0:
            raise ValueError("Tarifa, horas y antigüedad no pueden ser negativos.")

    def gross_salary(self) -> Money:
        # Solo las horas posteriores a 40 reciben el recargo de tiempo extra.
        regular_hours = min(self.hours_worked, Decimal("40"))
        overtime_hours = max(self.hours_worked - Decimal("40"), ZERO)
        return regular_hours * self.hourly_rate + overtime_hours * self.hourly_rate * Decimal("1.5")

    def employer_food_benefit(self) -> Money:
        return ZERO

    def savings_deposit(self) -> Money:
        # El ahorro se deposita solo con antigüedad superior a un año y consentimiento.
        if self.years_of_service > 1 and self.accepts_savings_fund:
            return self.gross_salary() * Decimal("0.02")
        return ZERO


@dataclass(frozen=True)
class CommissionEmployee:
    employee_id: str
    name: str
    base_salary: Money
    sales: Money
    commission_rate: Money

    def __post_init__(self) -> None:
        validate_identity(self.employee_id, self.name)
        if self.base_salary < ZERO or self.sales < ZERO:
            raise ValueError("El salario base y las ventas no pueden ser negativos.")
        if not ZERO <= self.commission_rate <= Decimal("1"):
            raise ValueError("La tasa de comisión debe estar entre 0 y 1.")

    def gross_salary(self) -> Money:
        # Tanto la comisión como el bono por ventas son parte del salario bruto.
        commission = self.sales * self.commission_rate
        sales_bonus = self.sales * Decimal("0.03") if self.sales > Decimal("20000000") else ZERO
        return self.base_salary + commission + sales_bonus

    def employer_food_benefit(self) -> Money:
        # Este valor corre por cuenta del empleador y no se suma al pago neto.
        return Decimal("1000000")

    def savings_deposit(self) -> Money:
        return ZERO


@dataclass(frozen=True)
class TemporaryEmployee:
    employee_id: str
    name: str
    monthly_salary: Money
    contract_months: int

    def __post_init__(self) -> None:
        validate_identity(self.employee_id, self.name)
        if self.monthly_salary < ZERO or self.contract_months <= 0:
            raise ValueError("El salario no puede ser negativo y el contrato debe durar al menos un mes.")

    def gross_salary(self) -> Money:
        return self.monthly_salary

    def employer_food_benefit(self) -> Money:
        return ZERO

    def savings_deposit(self) -> Money:
        return ZERO

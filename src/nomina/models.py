"""Tipos de valor que utiliza el servicio de nómina."""

from dataclasses import dataclass
from decimal import Decimal

Money = Decimal


@dataclass(frozen=True)
class PayrollResult:
    employee_id: str
    employee_name: str
    gross_salary: Money
    social_pension_deduction: Money
    arl_deduction: Money
    savings_deposit: Money
    net_salary: Money
    employer_food_benefit: Money

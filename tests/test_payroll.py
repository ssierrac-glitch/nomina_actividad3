"""Pruebas unitarias de las reglas y validaciones del sistema."""

import unittest
from decimal import Decimal

from nomina.employees import CommissionEmployee, HourlyEmployee, SalariedEmployee, TemporaryEmployee
from nomina.payroll import PayrollService

D = Decimal


class PayrollTests(unittest.TestCase):
    def setUp(self):
        self.payroll = PayrollService(arl_rate=D("0.01"))

    def test_salaried_bonus_starts_after_five_years(self):
        at_five = SalariedEmployee("1", "Ana", D("3000000"), 5)
        after_five = SalariedEmployee("2", "Eva", D("3000000"), 6)
        self.assertEqual(self.payroll.calculate(at_five).gross_salary, D("3000000.00"))
        result = self.payroll.calculate(after_five)
        self.assertEqual(result.gross_salary, D("3300000.00"))
        self.assertEqual(result.social_pension_deduction, D("132000.00"))
        self.assertEqual(result.arl_deduction, D("33000.00"))
        self.assertEqual(result.employer_food_benefit, D("1000000.00"))
        self.assertEqual(result.net_salary, D("3135000.00"))

    def test_hourly_overtime_uses_one_and_a_half_rate(self):
        employee = HourlyEmployee("3", "Luis", D("10000"), D("45"))
        result = self.payroll.calculate(employee)
        self.assertEqual(result.gross_salary, D("475000.00"))
        self.assertEqual(result.employer_food_benefit, D("0.00"))

    def test_hourly_savings_requires_more_than_one_year_and_consent(self):
        eligible = HourlyEmployee("4", "Mia", D("10000"), D("40"), 2, True)
        not_eligible = HourlyEmployee("5", "Noa", D("10000"), D("40"), 1, True)
        result = self.payroll.calculate(eligible)
        self.assertEqual(result.savings_deposit, D("8000.00"))
        self.assertEqual(result.net_salary, D("372000.00"))
        self.assertEqual(self.payroll.calculate(not_eligible).savings_deposit, D("0.00"))

    def test_commission_and_sales_bonus_are_in_gross(self):
        employee = CommissionEmployee("6", "Sol", D("1000000"), D("21000000"), D("0.05"))
        result = self.payroll.calculate(employee)
        self.assertEqual(result.gross_salary, D("2680000.00"))
        self.assertEqual(result.employer_food_benefit, D("1000000.00"))

    def test_sales_bonus_is_not_paid_at_exact_threshold(self):
        employee = CommissionEmployee("7", "Paz", D("1000000"), D("20000000"), D("0.05"))
        self.assertEqual(self.payroll.calculate(employee).gross_salary, D("2000000.00"))

    def test_temporary_employee_gets_no_benefits(self):
        result = self.payroll.calculate(TemporaryEmployee("8", "Ian", D("2000000"), 3))
        self.assertEqual(result.gross_salary, D("2000000.00"))
        self.assertEqual(result.employer_food_benefit, D("0.00"))

    def test_negative_hours_sales_salary_and_invalid_contract_are_rejected(self):
        with self.assertRaises(ValueError):
            HourlyEmployee("9", "A", D("10000"), D("-1"))
        with self.assertRaises(ValueError):
            CommissionEmployee("10", "B", D("0"), D("-1"), D("0.05"))
        with self.assertRaises(ValueError):
            SalariedEmployee("11", "C", D("-1"), 1)
        with self.assertRaises(ValueError):
            TemporaryEmployee("12", "D", D("1"), 0)

    def test_negative_net_is_rejected(self):
        employee = HourlyEmployee("13", "E", D("100"), D("1"))
        with self.assertRaises(ValueError):
            PayrollService(arl_rate=D("1")).calculate(employee)


if __name__ == "__main__":
    unittest.main()

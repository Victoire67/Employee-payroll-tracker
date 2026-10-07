from employee_payroll_tracker.utils import calculate_salary , apply_tax , generate_payslip
from employee_payroll_tracker.employee import Employee

class Payroll :
    def __init__(self):
        self._employees : list[Employee] = []

    def add_employee(self, employee : Employee):
        self._employees.append(employee)

    def remove_employee(self , employee : Employee ) -> None :
        self._employees.remove(employee)

    def total_tax(self) -> int : 
        return sum(e.tax for e in self._employees)

    def total_cost(self) -> int : 
        return sum(calculate_salary(e) for e in self._employees)

    def run(self) -> list[str]:
        return [generate_payslip(e) for e in self._employees]

    
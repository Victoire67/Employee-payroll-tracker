from utils import calculate_salary , apply_tax , generate_payslip
from employee import Employee

class Payroll :
    def __init__(self , employees):
        self._employees : list[Employee] = employees

    def add_employee(self, employee : Employee):
        self._employees.append(employee)

    def remove_employee(self , employee : Employee ) -> None :
        self._employees.remove(employee)

    def total_tax(self) -> int : 
        return sum(e.tax for e in self._employees)

    def total_cost(self) -> int : 
        return sum(calculate_salary(e) for e in self._employees)

    def run(self) -> list[str]:
        # print(self._employees);
        for employee in self._employees : 
            print(f"EMLOYEE {employee}")
            generate_payslip(employee)
        pass
        # return [generate_payslip(e) for e in self._employees]

    
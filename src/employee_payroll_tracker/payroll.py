from .utils import calculate_salary, generate_payslip
from .employee import Employee


class Payroll:
    def __init__(self, employees):
        self._employees: list[Employee] = list(employees)

    @property
    def employees(self) -> list[Employee]:
        # Return a copy so callers can't change the internal list directly.
        return list(self._employees)

    def count(self) -> int:
        return len(self._employees)

    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def find_employee(self, name: str) -> Employee | None:
        for employee in self._employees:
            if employee.name.lower() == name.lower():
                return employee
        return None

    def remove_employee(self, name: str) -> None:
        employee = self.find_employee(name)
        if employee is None:
            raise KeyError(f"No employee named {name}")
        self._employees.remove(employee)

    def total_tax(self) -> int:
        return sum(e.tax for e in self._employees)

    def total_cost(self) -> int:
        return sum(calculate_salary(e) for e in self._employees)

    def run(self) -> None:
        for employee in self._employees:
            generate_payslip(employee)

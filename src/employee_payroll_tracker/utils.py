from employee_payroll_tracker.employee import Employee


def calculate_salary(employee: Employee):
    return employee.salary + employee.bonus


def apply_tax(employee: Employee):
    return employee.salary - employee.tax


def generate_payslip(employee: Employee):
    return (
        f"Type:   {type(employee).__name__}\n"
        f"Salary: {employee.salary}\n"
        f"Bonus:  {employee.bonus}\n"
        f"Tax:    {employee.tax}\n"
        f"Net:    {calculate_salary(employee)}"
    )

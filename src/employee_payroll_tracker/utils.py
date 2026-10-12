from .employee import Employee


def calculate_salary(employee: Employee):
    return employee["salary"] + employee["bonus"]



def generate_payslip(employee: Employee):
    print(employee)
    print(
        f"Name:   {(employee["name"])}\n"
        f"Kind:   {(employee["KIND"])}\n"
        f"Salary: {employee["salary"]}\n"
        f"Bonus:  {employee["bonus"]}\n"
        f"Tax:    {employee["tax"]}\n"
        f"Net:    {calculate_salary(employee)}\n"
        f"==============================================================="
    )

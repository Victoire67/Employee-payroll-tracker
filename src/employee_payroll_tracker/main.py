from .employee import FullTimeEmployee, ContractEmployee, Intern
from .payroll import Payroll

# The number the user types -> the class that gets created.
EMPLOYEE_TYPES = {
    "1": FullTimeEmployee,
    "2": ContractEmployee,
    "3": Intern,
}

MENU = """
=========== PAYROLL MENU ===========
1. Add employee
2. Remove employee
3. List employees
4. Count employees
5. Show total tax
6. Show total cost
7. Run payroll (print payslips)
0. Exit
===================================="""


def ask_int(prompt: str) -> int:
    # Keep asking until the user types a whole number.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number, e.g. 750000")


def add_employee(payroll: Payroll) -> None:
    print("Employee type:")
    for key, employee_class in EMPLOYEE_TYPES.items():
        print(f"  {key}. {employee_class.KIND}")

    employee_class = EMPLOYEE_TYPES.get(input("Choose a type: ").strip())
    if employee_class is None:
        print("Invalid type, back to the menu.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if payroll.find_employee(name) is not None:
        print(f"An employee named '{name}' already exists.")
        return

    salary = ask_int(f"Salary (min {employee_class.MIN_SALARY}): ")
    bonus = ask_int(f"Bonus (min {employee_class.MIN_BONUS}): ")
    tax = ask_int("Tax (less than half the salary): ")

    # The property setters in employee.py raise ValueError on invalid values.
    try:
        employee = employee_class(salary, bonus, tax, name)
    except ValueError as error:
        print(f"Could not add employee: {error}")
        return

    payroll.add_employee(employee)
    print(f"{employee.KIND} '{employee.name}' added.")


def remove_employee(payroll: Payroll) -> None:
    name = input("Name of the employee to remove: ").strip()
    try:
        payroll.remove_employee(name)
    except KeyError as error:
        print(error.args[0])
        return
    print(f"'{name}' removed.")


def list_employees(payroll: Payroll) -> None:
    if payroll.count() == 0:
        print("No employees yet.")
        return
    for number, employee in enumerate(payroll.employees, start=1):
        print(f"{number}. {employee.name} | {employee.KIND} | salary {employee.salary}")


def count_employees(payroll: Payroll) -> None:
    print(f"Number of employees: {payroll.count()}")


def show_total_tax(payroll: Payroll) -> None:
    print(f"Total tax: {payroll.total_tax()}")


def show_total_cost(payroll: Payroll) -> None:
    print(f"Total cost (salary + bonus): {payroll.total_cost()}")


def run_payroll(payroll: Payroll) -> None:
    if payroll.count() == 0:
        print("No employees to pay.")
        return
    payroll.run()
    show_total_tax(payroll)
    show_total_cost(payroll)


# The number the user types -> the function that handles it.
ACTIONS = {
    "1": add_employee,
    "2": remove_employee,
    "3": list_employees,
    "4": count_employees,
    "5": show_total_tax,
    "6": show_total_cost,
    "7": run_payroll,
}


def main() -> int:
    payroll = Payroll([])

    try:
        while True:
            print(MENU)
            choice = input("Choose an option: ").strip()

            if choice == "0":
                print("Goodbye!")
                return 0

            action = ACTIONS.get(choice)
            if action is None:
                print("Invalid option, try again.")
                continue

            action(payroll)
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or end of input: exit cleanly instead of a traceback.
        print("\nGoodbye!")
        return 0


# __name__ is what is known as the dunder variable , which stores the name of the current execution context 
# python will assign the name of the file when we are working with the file . 

if __name__ == "__main__":
    main()

# Employee Payroll Tracker

A command-line app for managing employees and running payroll.

## Requirements

- Python 3.14+
- Poetry

## Setup

```bash
poetry install
```

## Run

```bash
poetry run python -m employee_payroll_tracker.main
```

## Features

- Add, remove, list and count employees
- Three employee types, each with a minimum salary and bonus:

  | Type       | Min salary | Min bonus |
  |------------|-----------:|----------:|
  | Full-time  | 700,000    | 20,000    |
  | Contract   | 500,000    | 10,000    |
  | Intern     | 350,000    | 7,000     |

- Tax must be less than half the salary
- Show total tax and total cost (salary + bonus)
- Run payroll to print a payslip for each employee

## Project Structure

```
src/employee_payroll_tracker/
├── employee.py   # Employee classes and validation
├── payroll.py    # Payroll class (stores and manages employees)
├── utils.py      # Salary calculation and payslips
└── main.py       # CLI menu
```

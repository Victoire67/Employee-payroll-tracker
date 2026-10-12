from .employee import Employee
from .payroll import Payroll


def main() -> int:

    salaries = list(range(4000000, 350000, -350000))
    taxes = list(range(40000, 3500, -3500))
    bonusies = list(range(60000, 5500, -5500))

    amali_tech = []

    i = 0
    while i < 10:
        amali_tech.append({
            "salary": salaries[i],
            "bonus": bonusies[i],
            "tax": taxes[i],
            "name" : "VIKI",
            "KIND" : "MUTTTU"
        })
        i += 1
    print(amali_tech[0])

    january = Payroll(amali_tech)

    january.run()


# __name__ is what is known as the dunder variable , which stores the name of the current execution context 
# python will assign the name of the file when we are working with the file . 

if __name__ == "__main__" : 
    main()
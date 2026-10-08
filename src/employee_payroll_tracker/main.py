from employee import Employee
from payroll import Payroll

salaries = list(range(4000000, 350000, -350000))
taxes = list(range(40000, 3500, -3500))
bonusies = list(range(60000, 5500, -5500))


amali_tech = []

i = 0
while i < 10:
    amali_tech.append({
        "salary": salaries[i],
        "bonus": bonusies[i],
        "tax": taxes[i]
    })
    i += 1
print(amali_tech[0])





january = Payroll(amali_tech)

january.run()

# print(amali_tech)
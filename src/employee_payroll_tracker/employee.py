class Employee:
    MIN_SALARY = 0 
    MIN_BONUS = 0 
    KIND = "Employee"

    def __init__(self, salary: int, bonus: int, tax: int , name):
        self.name = name       
        self.salary = salary
        self.bonus = bonus
        self.tax = tax
        

    @property
    def salary(self):
        return self._salary

    @property
    def bonus(self):
        return self._bonus

    @property
    def tax(self):
        return self._tax

    @salary.setter
    def salary(self, value):
        if value < self.MIN_SALARY:
            raise ValueError(f"Salary should not be below {self.MIN_SALARY}")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value > 0:
            self._bonus = value
            return
        raise ValueError("The value of bonus should be at least 1 or more")

    @tax.setter
    def tax(self, value):
        if value > 1:
            self._tax = value
            return
        raise ValueError("Every employee should be taxed a valid value")


class FullTimeEmployee(Employee):
    MIN_SALARY, MIN_BONUS, KIND = 700_000, 20_000, "Full-time employee"

    @property
    def salary(self):
        return self._salary

    @property
    def bonus(self):
        return self._bonus

    @property
    def tax(self):
        return self._tax

    @salary.setter
    def salary(self, value):
        if value < self.MIN_SALARY:
            raise ValueError(f"A Full time employee earns {self.MIN_SALARY} and above")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value < self.MIN_BONUS:
            raise ValueError(
                f"A full time employee should have a bonus worth {self.MIN_BONUS} and above")
        self._bonus = value

    @tax.setter
    def tax(self, value):
        if (value >= self._salary / 2):
            raise ValueError("Tax should be less than half the salary")
        self._tax = value


class ContractEmployee(Employee):
    MIN_SALARY, MIN_BONUS, KIND = 500_000, 10_000, "Contract employee"
    @property
    def salary(self):
        return self._salary

    @property
    def bonus(self):
        return self._bonus

    @property
    def tax(self):
        return self._tax

    @salary.setter
    def salary(self, value):
        if value < self.MIN_SALARY:
            raise ValueError(f"A Full time employee earns {self.MIN_SALARY} and above")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value < self.MIN_BONUS:
            raise ValueError(
                f"A full time employee should have a bonus worth {self.MIN_BONUS} and above")
        self._bonus = value

    @tax.setter
    def tax(self, value):
        if (value >= self._salary / 2):
            raise ValueError("Tax should be less than half the salary")
        self._tax = value


class Intern(Employee):
    MIN_SALARY, MIN_BONUS, KIND = 350_000, 7_000, "Intern"
    @property
    def salary(self):
        return self._salary

    @property
    def bonus(self):
        return self._bonus

    @property
    def tax(self):
        return self._tax

    @salary.setter
    def salary(self, value):
        if value < self.MIN_SALARY:
            raise ValueError(f"A Full time employee earns {self.MIN_SALARY} and above")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value < self.MIN_BONUS:
            raise ValueError(
                f"A full time employee should have a bonus worth {self.MIN_BONUS} and above")
        self._bonus = value

    @tax.setter
    def tax(self, value):
        if (value >= self._salary / 2):
            raise ValueError("Tax should be less than half the salary")
        self._tax = value

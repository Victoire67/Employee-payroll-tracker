class Employee:

    def __init__(self, salary: int, bonus: int, tax: int):
        self._salary = salary
        self._bonus = bonus
        self._tax = tax

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
        print(f"Giving salary the value of {value}")
        if value < 700000:
            raise ValueError("Salary should not be below zero")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if self._bonus > 0:
            self._bonus = value
            return
        raise ValueError("The value of bonus should be at least 1 or more")

    @tax.setter
    def tax(self, value):
        if self._tax > 1:
            self._tax = value
            return
        raise ValueError("Every employee should be taxed a valid value")


class FullTimeEmployee(Employee):
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
        if value < 700000:
            raise ValueError("A Full time employee earns 700K and above")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value < 20000:
            raise ValueError(
                "A full time employee should have a bonus worth 20k and above")
        self._bonus = value

    @tax.setter
    def tax(self, value):
        if (value >= self._salary / 2):
            raise ValueError("Tax should be less than half the salary")
        self._tax = value


class ContractEmployee(Employee):
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
        if value < 500000:
            raise ValueError("A Full time employee earns 700K and above")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value < 10000:
            raise ValueError(
                "A full time employee should have a bonus worth 20k and above")
        self._bonus = value

    @tax.setter
    def tax(self, value):
        if (value >= self._salary / 2):
            raise ValueError("Tax should be less than half the salary")
        self._tax = value


class Intern(Employee):

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
        if value < 350000:
            raise ValueError("A Full time employee earns 700K and above")
        self._salary = value

    @bonus.setter
    def bonus(self, value):
        if value < 7000:
            raise ValueError(
                "A full time employee should have a bonus worth 20k and above")
        self._bonus = value

    @tax.setter
    def tax(self, value):
        if (value >= self._salary / 2):
            raise ValueError("Tax should be less than half the salary")
        self._tax = value

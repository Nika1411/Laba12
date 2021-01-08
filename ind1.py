#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 14
# Создать класс Payment (зарплата). В классе должны быть представлены поля: фамилия-
# имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и
# удержанная суммы. Реализовать методы: вычисления начисленной суммы, вычисления
# удержанной суммы, вычисления суммы, выдаваемой на руки, вычисления стажа. Стаж
# вычисляется как полное количество лет, прошедших от года поступления на работу, до теку-
# щего года. Начисления представляют собой сумму, начисленную за отработанные дни, и
# надбавки, то есть доли от первой суммы. Удержания представляют собой отчисления в
# пенсионный фонд (1% от начисленной суммы) и подоходный налог. Подоходный налог
# составляет 13% от начисленной суммы без отчислений в пенсионный фонд.

class Payment:

    def __init__(self, full_name=' ', salary=0, year=0, percent=0, days_worked=0, working_days=1):
        self.full_name = str(full_name)
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.days_worked = int(days_worked)
        self.working_days = int(working_days)
        # self.amount = 0
        # self.held_amount = 0
        # self.hand_amount = 0
        # self.exp = 0

        # self.accrued_amount()
        # self.withheld_amount()
        # self.handed_amount()
        # self.experience()

    def read(self):
        full_name = input('Введите  имя: ')
        salary = input('Введите зарплату: ')
        year = input('Введите год вступления ')
        percent = input('Введите процент премии: ')
        days_worked = input('Введите количество отработанных дней в месяце: ')
        working_days = input('Введите количество рабочих дней в месяце: ')

        self.full_name = full_name
        self.salary = int(salary)
        self.year = int(year)
        self.percent = float(percent)
        self.days_worked = int(days_worked)
        self.working_days = int(working_days)

        # self.accrued_amount()
        # self.withheld_amount()
        # self.handed_amount()
        # self.experience()

    def display(self):
        print(f"{self.full_name}")
        print(f"{self.salary}")
        print(f"{self.year}")
        print(f"{self.percent}")
        print(f"{self.days_worked}")
        print(f"{self.working_days}")
        # print(f"Сумма удержания: {round(self.held_amount)}")
        # print(f"Рассчитанная выданная сумма: {round(self.hand_amount)}")
        # print(f"Опыт: {self.exp} year(s)")

    def accrued_amount(self):
        a = self.salary / self.working_days
        b = a * self.days_worked
        percent = self.percent / 100 + 1
        # self.amount = b * percent
        return b * percent

    def withheld_amount(self):
        b = (self.salary / self.working_days) * self.days_worked
        # self.held_amount = b * (0.13 + 0.01)
        return b * (0.13 + 0.01)

    def handed_amount(self):
        a = self.salary / self.working_days
        b = a * self.days_worked
        percent = self.percent / 100 + 1
        # self.hand_amount = self.amount - self.held_amount
        return b * percent - (self.salary / self.working_days) * self.days_worked

    def experience(self):
        # self.exp = 2021 - self.year
        return 2021 - self.year


if __name__ == '__main__':
    r1 = Payment()
    r1.read()
    r1.display()
    print(r1.accrued_amount())
    print(r1.withheld_amount())
    print(r1.handed_amount())
    print(r1.experience())

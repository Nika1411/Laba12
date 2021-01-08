#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 15
# Создать класс Triad (тройка чисел); определить методы увеличения полей на 1. Определить
# класс-наследник Time с полями: час, минута, секунда. Переопределить методы увеличения
# полей на 1 и определить методы увеличения на n секунд и минут.

class Triad:

    def __init__(self, first=1, second=1, third=1):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    def read(self):
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        third = input('Введите третье число: ')

        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    def sum1(self):
        return self.first + 1

    def sum2(self):
        return self.second + 1

    def sum3(self):
        return self.third + 1


class Time(Triad):
    def __init__(self, first=20, second=59, third=59, n_minutes=0, n_seconds=1):
        super(Time, self).__init__(first, second, third)
        self.__first = first
        self.__second = second
        self.__third = third
        self.__a = int(n_minutes)
        self.__b = int(n_seconds)

    def sum1(self):
        return self.first + 1

    def sum2(self):
        return self.second + 1

    def sum3(self):
        return self.third + 1

    def display(self):
        print(f"{self.__first}(ч)., {self.__second}(мин)., {self.__third}(сек).")

    def mul(self, new):
        if isinstance(new, Time):
            hour = self.__first + 1
            minutes = self.__second + 1 + self.__a
            seconds = self.__third + 1 + self.__b

            if seconds >= 60:
                minutes += seconds // 60
                seconds %= 60

            if minutes >= 60:
                hour += minutes // 60
                minutes %= 60

            return Time(hour, minutes, seconds)
        else:
            raise ValueError()


if __name__ == '__main__':
    r1 = Triad()
    r1.read()
    print(r1.sum1())
    print(r1.sum2())
    print(r1.sum3())

    m1 = Time()
    m1.display()

    m2 = Time()

    m3 = m2.mul(m1)
    m3.display()

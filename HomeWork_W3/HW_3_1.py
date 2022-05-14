class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        assert den != 0, "Denominator can't be zero"
        self.__den = den

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return self.__class__(num, den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return self.__class__(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return self.__class__(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return self.__class__(num, den)

    def __str__(self):
        return f'{self.num} / {self.den}'


class Mixin:
    @staticmethod
    def sub(fraction1, fraction2):
        num = fraction1.num * fraction2.den - fraction1.den * fraction2.num
        den = fraction1.den * fraction2.den
        return f'{num} / {den}'

    @staticmethod
    def add(fraction1, fraction2):
        num = fraction1.num * fraction2.den + fraction1.den * fraction2.num
        den = fraction1.den * fraction2.den
        return f'{num} / {den}'

    @staticmethod
    def mul(fraction1, fraction2):
        num = fraction1.num * fraction2.num
        den = fraction1.den * fraction2.den
        return f'{num} / {den}'

    @staticmethod
    def truediv(fraction1, fraction2):
        num = fraction1.num * fraction2.den
        den = fraction1.den * fraction2.num
        return f'{num} / {den}'

    @classmethod
    def string(cls, value):
        values = [int(x) for x in value.split('/')]
        assert len(values) == 2
        return cls(*values)


class MixedFraction(Fraction, Mixin):
    pass


fr1 = MixedFraction(3, 5)
fr2 = MixedFraction(8, 6)

print(f'{fr1.num} / {fr1.den} and {fr2.num} / {fr2.den}\n')

print(f'Sub: {fr1 - fr2}',
      f'Add: {fr1 + fr2}',
      f'Mul: {fr1 * fr2}',
      f'Truediv: {fr1 / fr2}', sep='\n')

fr3 = MixedFraction.string('3/5')
fr4 = MixedFraction.string('8/6')

print(f'\n{fr3} and {fr4}\n')

print(f'Sub: {MixedFraction.sub(fr3, fr4)}',
      f'Add: {MixedFraction.add(fr3, fr4)}',
      f'Mul: {MixedFraction.mul(fr3, fr4)}',
      f'Truediv: {MixedFraction.truediv(fr3, fr4)}', sep='\n')


# Створити клас дріб (Fraction), конструктор якого приймає цілі числа
# (num, den - чисельник (numerator), знаменник (denominator)).
#
# Виконати:
#
# Атрибути чисельник та знаменник у класі зробити приватними.
# Доступ до атрибутів продати через характеристики.
#
# Перевизначити методи __sub__, __add__, __mull__, __truediv__
# для того, щоб можна було виконувати відповідні математичні дії з об'єктами класу дріб.
# (Віднімання, складання, множення та розподіл).
#
# Додати клас міксину, в якому реалізувати статичні методи, для цих операцій
# (add, sub, mull, div). Додати клас міксин до класу Fraction
#
# Створити classmethod котрий з рядка типу 'числитель/знаменник'
# повертає об'єкт класу дріб.
#
# Перевизначити метод __str__, який при виведенні об'єкта на друк виводитиме рядок виду num/den.
#
# Створити об'єкти класу дріб.
#
# Виконати усі реалізовані методи.

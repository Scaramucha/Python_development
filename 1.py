# Создать функцию деления, Описать ошибку деления на 0.
def division_f(a, b):
    if b == 0:
        try:
            a / b
        except ZeroDivisionError:
            return 'На 0 делить нельзя.'
    elif b != 0:
        x = a / b
        return x
print(division_f(int(input('Первое число')), int(input('Второе число'))))
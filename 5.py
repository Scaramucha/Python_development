# Получить числа через пробел, найти их сумму
# Получить ещё числа, сложить их с суммой предыдущего
# Продолжать до стопслова. Если оно в строке с числами - прибавить сумму чисел и выйти из цикла.
the_end = False
amount = 0
while the_end == False:
    message = input("Введите числа для сложения. Для завершения введите *.").split()
    if '*' in message:
        the_end = True
    else:
        the_end = False
    sum_gap = [int(i) for i in message if i.isdigit()]
    amount = amount + sum(sum_gap)
    print("Общая сумма:", amount)
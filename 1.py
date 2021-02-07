# Вывести Типы зачений списка через type()
a = ['m', 69, ('r', 6), 1.67, [3, 't'], {'qwert', 44}, True, (3 + 4j)]
i = 0
while i < len(a) :
    print(type(a[i]))
    i = i + 1
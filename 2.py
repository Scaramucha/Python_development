#Создать массив из символов пользователя и поменяь парные соседние местами
usertext = input('Enter text')
element = list(usertext)
print(element)
a = element[::2]
b = element[1::2]
new_element = []
i = 0
if len(a) == len(b):
    while i < len(b):
        new_element.append(b[i])
        new_element.append(a[i])
        i = i + 1
else:
    while i < len(b):
        new_element.append(b[i])
        new_element.append(a[i])
        i = i + 1
    new_element.append(a[i])
print(new_element)

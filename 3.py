#Выдавать пользователю сезон по номеру месяца + list + dict
season = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
month = {'one' : 'Winter', 'two' : 'Spring', 'three': 'Summer', 'four' : 'Autumn'}
a = int(input('Enter month number'))
if a in season[0]:
    print('This is', month['one'])
elif a in season[1]:
    print('This is', month['two'])
elif a in season[2]:
    print('This is', month['three'])
elif a in season[3]:
    print('This is', month['four'])
#Добавить в действующий рейтинг значение, сохраняя целостность рейтинга - убывание
rating = [9, 8, 4, 3, 3]
new_element = int(input("Enter a new rating item."))
rating.append(new_element)
rating.sort()
rating.reverse()
print(rating)
#for elem in rating:
#    if new_element > elem:
#        rating.insert(rating.index(elem), new_element)
#        break
#    elif elem == rating[-1]:
#        rating.append(new_element)
#        break
#Через индексы для тренировки
# Создать функцию, которая принимает личные данные пользователя, как именованные аргуметы. Сделать вывод одной строкой.
def card(name = input("Имя"), surname = input("Фамилия"), year_of_birth = input("Год рождения"), city = input("Город проживания"), mail = input("e-mail"), phone = input('Номер телефона')):
    business_card = [name, surname, year_of_birth, city, mail, phone]
    return " ".join(business_card)
print(card())
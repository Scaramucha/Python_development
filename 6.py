# Функция, принимающая слова из маленьких латинских букв и возвращающую с прописной первой.
def my_func(text = input("Ведите слова маленькими буквамию")):
    if text.islower() == True:
       return text.title()
    else:
        return "Символы не соответствуют условию"
print(my_func())

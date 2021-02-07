#Выводить ввведённые пользователем слова построчно + нумерация, + обрезка длинных(>10 симвлов)
text = input('Enter text')
words = text.split()
print(words)
for b, a in enumerate(words):
    print(f'{b + 1} {a[:10]}')
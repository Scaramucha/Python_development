number = False
while number <= 0:
    number = int(input("Enter a positive integer"))
print(number)
count = 1
digit = 0
while number // count > 0:
    count = count * 10
    digit = digit + 1
digit = digit - 1
print(digit)
value = []
while digit >= 0:
    num = number // (10 ** digit)
    value.append(num)
    number = number - num * (10 ** digit)
    digit = digit - 1
print(value)
a = 9
while True:
    if (a in value):
        print("Maximum number is", a, ".")
        break
    else:
        a = a - 1
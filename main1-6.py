result = float(input("Result on the first day."))
desired_result = float(input("Desired result."))
day = 1
while result < desired_result:
    result = result * 1.1
    day =day + 1
print("The result will be achieved on the", day, "day.")

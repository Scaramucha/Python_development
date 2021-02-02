proceeds = float(input("Enter the amount of proceeds."))
costs = float(input("Enter the amount of costs."))
profit = proceeds - costs
if profit > 0:
    print("The enterprise makes a profit.")
elif profit < 0:
    print(" The enterprise makes losses.")
elif profit == 0:
    print("The entrprise did not icur losses, but did not make a profit either.")
if profit > 0:
    profitability = round(profit / proceeds, 3)
    print("The profitability of the enterprise is", profitability, ".")
    staff = int(input("Indicate the number of employees in the enterprise."))
    staff_profit = round(profit / staff, 2)
    print("Profit per employee of the enterprise is:", staff_profit, ".")
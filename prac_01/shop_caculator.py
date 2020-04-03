total = 0
number = int(input("Enter number of items:"))
while number <= 0:
    print("Invalid number of items!")
    number = int(input("Enter number of items:"))


if number > 0:
    for i in range(number):
        price = int(input("Enter price of item:"))
        total += price
    if total > 100:
        total *= 0.9  # apply 10% discount
    print("Total price for {} items is ${:.2f}".format(number, total))  # formatting for currency output

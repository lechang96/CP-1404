"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))  # ask for sales
while sales >= 0:  # calculate user's bonus using while loops
    if sales < 1000:
        price = sales * 0.1
        print("You get a 10% bonus, which is ${} ".format(price))
    else:
        price = sales * 0.15
        print("You get a 15% bonus, which is ${} ".format(price))
    sales = float(input("Enter sales: $"))

print("Invalid Number!")

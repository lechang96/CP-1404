import random

out_file = open("OUTPUT_FILE.py", 'w')

days = 0
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0


price = INITIAL_PRICE
print("Starting Price:${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    price_charge = random.randint(1, 2)

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    days += 1
    price *= (1 + price_change)

    print("On day {} price is: ${:,.2f}".format(days,price), file=out_file)
    print()

out_file.close()
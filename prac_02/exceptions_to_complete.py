
finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a integer:"))
        break
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)


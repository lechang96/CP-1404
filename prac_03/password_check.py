while True:
    password = input("Enter a password:")
    if len(password) < 10:
        print("Your password must be at least 10 characters")
        continue
    else:
        display_pw = "*" * len(password)
        print("Your password is: {}".format(display_pw))
        break
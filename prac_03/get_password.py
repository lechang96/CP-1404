def main():
    while True:
        password = get_password()
        if len(password) < 10:
            print("Your password must be at least 10 characters")
            continue
        else:
            display_pw = display_password(password)
            print("Your password is: {}".format(display_pw))
            break


def get_password():
    password = input("Enter a password:")
    return password


def display_password(password):
    display_pw = "*" * len(password)
    return display_pw


main()
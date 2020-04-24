from prac_06.guitar import Guitar


def main():
    """Test whether Guitar class works"""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 97, guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))


if __name__ == '__main__':
    main()

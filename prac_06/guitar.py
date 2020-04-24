CURRENT_YEAR = 2019
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of the guitar"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is 50 or more years old,"""
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """used for sorting Guitars - by year released."""
        return self.year < other.year



class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name="", typing="", reflection="", year =0):
        """Initialise a programming instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the programming is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string of the programming"""
        return "{}, Dynamic Typing, Reflection = {}, First appeared in {}".format(self.name,self.is_dynamic,self.year)



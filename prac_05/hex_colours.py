
colours = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "azure1": "#f0ffff",
           "azure2": "#e0eeee", "azure3": "#c1cdcd", "beige": "#f5f5dc", "blueviolet": "#8a2be2",
           "blue1": "#0000ff",
           "black": "#000000", "chocolate": "#d2691e"}

colour_name = input("Enter a colour name:").lower()

while colour_name != "":
    print("{} is {}".format(colour_name, colours.get(colour_name)))
    colour_name = input("Enter a colour name:").lower()
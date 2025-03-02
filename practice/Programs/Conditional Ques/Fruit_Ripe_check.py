"""
 Fruit Ripeness Checker
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
"""

fruit = "banana"
color = input("Color is ")

if fruit == "banana":
    if color == "green":
        print("Banana is unripe.")
    elif color == "yellow":
        print("Banana is ripe.")
    elif color == "brown":
        print("Banana is overripe.")
    else:
        print("Invalid color input.")




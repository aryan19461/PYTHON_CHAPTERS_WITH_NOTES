"""
 Validate Input
Problem: Keep asking the user for input until they enter a number between 1 and 10.
"""

inputNumber = int(input("Enter the number  between 1 -10 : "))

while inputNumber in range(1,11):
    if inputNumber in range(1,11):
        print("Number is Between the range")
        break
    else:
        print("Not in Range")
        break;

    

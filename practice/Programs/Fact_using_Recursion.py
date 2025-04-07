number = int(input("Enter the number = "))

def FactRecursion(number):
    if number == 0:
        return 1
    else:
        return number * FactRecursion(number-1)

print(f"Factorial is : {FactRecursion(number)}")
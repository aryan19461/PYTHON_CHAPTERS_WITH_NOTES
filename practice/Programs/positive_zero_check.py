number = int(input("Enter number = "))

def check(number):
    if number < 1 and number > -1:
        print(f"Entered number {number} is Zero")
        return
    elif number < 0:
        print(f"Entered number {number} is a Negative number")
        return


check(number)
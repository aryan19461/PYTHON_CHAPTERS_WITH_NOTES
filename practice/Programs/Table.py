number = int(input("Enter the number for table = "))
def table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table(number)
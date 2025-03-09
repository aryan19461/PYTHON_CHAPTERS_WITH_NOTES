a = int(input("Enter first variable = "))
b = int(input("Enter second variable = "))

def swap(a,b):
    temp = a
    a = b
    b = temp
    print("Swapping" ,a,b)

swap(a,b)
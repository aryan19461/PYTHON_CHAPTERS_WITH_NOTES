first = int(input("Enter the first number = "))
second = int(input("Enter the second number = "))

def calHCF(first, second):
    if first>second:
        smaller = second
    else :
        smaller = first
    for i in range (1,smaller+1):
        if ( (first % i==0) and (second % i == 0) ):
            hcf = i
    return hcf

print(f"HCF of {first} and {second} is " , calHCF(first, second))




n = int(input("Enter the decimal number for conversion to BINARY :"))
def DecToBinary(n):
    if n > 1:
        DecToBinary(n//2)
    print(n%2,end="")
print("Binary :",end=" ")
DecToBinary(n)
"""
armstrong number =
153 = (1*1*1) + (5*5*5) + (3*3*3)
    = 1 + 125 + 27
    = 153
    therefore armstrong number

"""
number = int(input("Enter the number = "))

def arm(number):
    sum = 0
    temp = number
    while temp >0:
        digit = temp %10
        cube = digit ** 3
        sum = sum + cube
        temp //= 10
    if sum ==number:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

print(arm(number))
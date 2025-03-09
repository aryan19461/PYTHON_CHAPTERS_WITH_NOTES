upper = int(input("Enter upper limit = "))
lower = int(input("Enter Lower limit = "))

for num in range(lower ,upper +1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10 #taking last value of digit eg 407 -> 7 is taken
        sum += digit ** order
        temp //= 10  #last digit remove
    if num == sum:
        print(num)


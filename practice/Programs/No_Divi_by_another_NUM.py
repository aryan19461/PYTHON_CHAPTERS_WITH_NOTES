x = int(input("Enter the number for which you want to find the divisibility numbers = "))
limit_x = int(input("Enter the number upto which the division shouold be possible = "))
for i in range(1,limit_x+1):
    if i % x==0:
        print(f"{i} / {x} is possible")



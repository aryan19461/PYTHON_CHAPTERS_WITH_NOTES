upperLimit=int(input("Upper limit of series is = "))
a =0
b=1
for i in range(1,upperLimit+1):
        c = a+b
        a =b
        b =c
        print(c)



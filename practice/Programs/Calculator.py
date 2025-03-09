x = int(input("Enter first number = "))
y = int(input("Enter second number = "))
print("Enter the operator sign \n")
op = input("  Additon  = +\n  Subtraction  = -\n  MOD  = %\n  Multiply  = *\n  Division  = /\n")

if op == "+":
    print(f"{x} + {y} is {x+y}")
elif op ==  "-":
    print(f"{x} - {y} is {x*y}")
elif op == "*":
    print(f"{x} * {y} is {x*y}")
elif op == "/":
    print(f"{x} / {y} is {x / y}")
elif op == "%":
    print(f"{x} % {y} is {x%y}")


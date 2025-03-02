"""
Factorial Calculator
Problem: Compute the factorial of a number using a while loop.
"""
number = int(input("Enter the number for the factorial : "))
fact =1
while number>0:
    fact = fact * number
    number=number -1
    print(fact)
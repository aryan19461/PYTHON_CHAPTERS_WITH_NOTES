"""
 Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.
"""

sum =0
n = int(input("Enter the range of number :  "))
for i in range(1,n+1):
    if i%2 == 0:
        sum = sum +i;
print(f"Sum of even numbers are : {sum}")
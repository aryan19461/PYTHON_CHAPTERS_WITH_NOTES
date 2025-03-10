'''
1. natural Number  : +ve integers
2. recursion -> when the function calls it itself

'''

n = int(input("Enter the upper limit of the number : "))
def NaturalSumREc(n):
    if n <=1:
        return n
    else:
        return n + NaturalSumREc(n-1)


print("The sum of natural numbers from 1 to", n, "is", NaturalSumREc(n))
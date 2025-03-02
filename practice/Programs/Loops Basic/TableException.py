
"""
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
"""

n = int(input("Enter the numebr for which you want the table : "))
for i in range(1,11):
    if i ==5 :
        pass
    else:
        print(f"{n} x {i} = {i*n}")


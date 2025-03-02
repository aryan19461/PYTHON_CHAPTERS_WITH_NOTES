"""
 Counting Positive Numbers
Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

"""

numbers = [1,2,-3,4,5,-1,-2,0,-4]
count = 0
for i in numbers :
    if i>=0:
        count=count+1;

print(f"Number of positive numbers in the list are : {count}")
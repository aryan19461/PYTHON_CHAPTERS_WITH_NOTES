
"""
Function with *args
Problem: Write a function that takes variable number of arguments and returns their sum.
"""
def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))

"""
Explanation of the Code:
The given code defines a function sum_all that takes a variable number of arguments using *args and returns their sum.

Breakdown of the Code:
python
Copy
Edit
def sum_all(*args):   # *args allows multiple arguments
    print(args)       # Printing args as a tuple
    for i in args:    # Loop through each argument
        print(i * 2)  # Multiply each argument by 2 and print it
    return sum(args)  # Return the sum of all arguments
python
Copy
Edit
print(sum_all(1, 2, 3))  # Function call with 3 arguments
Output:
bash
Copy
Edit
(1, 2, 3)   # args is a tuple (1, 2, 3)
2           # 1 * 2
4           # 2 * 2
6           # 3 * 2
6           # sum(1, 2, 3) = 6
What is *args in Python?
In Python, *args is used in function definitions to allow arbitrary numbers of positional arguments to be passed into the function.

Syntax:
python
Copy
Edit
def function_name(*args):
    # Function body
The * before args tells Python to collect all positional arguments into a tuple.
The name args is not mandatory—you can use any variable name after *, but args is a convention.

"""
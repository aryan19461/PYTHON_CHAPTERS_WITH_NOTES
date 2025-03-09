"""
What is **kwargs in Python?
In Python, **kwargs allows you to pass a variable number of keyword arguments to a function. It collects them into a dictionary.

Syntax:
        def function_name(**kwargs):
            # Function body
The ** before kwargs tells Python to collect all named (keyword) arguments into a dictionary.
Like args, kwargs is a convention—you can name it anything (**data, **info, etc.), but kwargs is commonly used.

"""

#Example 1: Function with **kwargs
def user_info(**kwargs):
    print(kwargs)

user_info(name="Alice", age=25, city="New York")
# NOTE --> order of arguments is not important as we can write city first then name also
#Here, **kwargs collects all keyword arguments into a dictionary. We can then access values using kwargs['key'].

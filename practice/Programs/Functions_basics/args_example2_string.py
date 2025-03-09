def introduce(name, *hobbies):
    print(f"My name is {name}.")
    print("My hobbies are:")
    for hobby in hobbies:
        print(f"- {hobby}")

introduce("John", "Reading", "Coding", "Gaming")

"""
Key Points:
   1)*args allows passing multiple arguments as a tuple.
   2)It is useful when the number of arguments is unknown.
   3)It works only for positional arguments (not keyword arguments).
   4)You can mix regular parameters and *args in function definitions.
"""
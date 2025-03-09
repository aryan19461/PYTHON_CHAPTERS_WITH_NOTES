#Example 2: Looping Through **kwargs [ #kwargs.items() gives key-value pairs, which we iterate over.]

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="Bob", age=30, country="USA")
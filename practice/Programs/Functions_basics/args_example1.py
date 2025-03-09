def multiply_all(*args):
    result = 1
    for num in args:
        result = result*num
    return result

print(multiply_all(2, 3, 4))  # Output: 24 (2*3*4)
print(multiply_all(5, 10))    # Output: 50 (5*10)

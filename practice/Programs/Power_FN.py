nterms = int(input("Enter the no of terms = "))
x = int(input("Enter the number for which the power has to be raised to = "))
result = list(
    map(lambda y : y**2, range(nterms+1))
          )
# map -> used when every iterables required to worked on
# list() -> result = list( ) this is used to put all these in a list

for i in range(nterms+1):
    print(f"the values of the {i} raised to power of {x} is {result[i]}")

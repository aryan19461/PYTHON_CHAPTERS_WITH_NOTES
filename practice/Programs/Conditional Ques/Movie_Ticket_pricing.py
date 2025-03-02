"""
Movie Ticket Pricing
Problem: Movie tickets are priced based on age: $20 for adults (18 and over), $10 for children. Everyone gets a discount on particular days given below.

if-else syntax (Optional single line syntax) --> price = 20 if age >= 18 else 10

"""
age = int(input("Enter the Age : "))
Day = input("""Enter the day :
    1) Monday (discount is none)
    2) Tuesday (discount is 2$)
    3) Wednesday (discount is 4$)
    4) Thursday (discount is 1$)
    5) Friday (discount is none)
    6) Saturday (discount is none)
    7) Sunday (discount is 5$)
""")
priceA = 20
priceC = 10
if Day == "Monday" :
    if age >= 18:
        print(f"price of the movie is {priceA}")
    else:
        print(f"Price is {priceC}")

if Day == "Tuesday" :
    if age >= 18:
        print(f"price of the movie is {priceA - 2}")
    else:
        print(f"Price is {priceC - 2}")

if Day == "Wednesday" :
    if age >= 18:
        print(f"price of the movie is {priceA - 4}")
    else:
        print(f"Price is {priceC-4}")

if Day == "Thursday" :
    if age >= 18:
        print(f"price of the movie is {priceA - 1}")
    else:
        print(f"Price is {priceC - 1}")

if Day == "Friday" :
    if age >= 18:
        print(f"price of the movie is {priceA}")
    else:
        print(f"Price is {priceC}")

if Day == "Saturday" :
    if age >= 18:
        print(f"price of the movie is {priceA}")
    else:
        print(f"Price is {priceC}")

if Day == "Sunday" :
    if age >= 18:
        print(f"price of the movie is {priceA - 5}")
    else:
        print(f"Price is {priceC-5}")

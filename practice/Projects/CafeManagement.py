#Defining the menu
menu ={
    'pizza' : 40,
    'pasta' : 50,
    'burger' : 60,
    'dessert' : 30,
    'coke' : 20,
    'water' : 10,
    'juice' : 15,
    'Tea' : 15
}
#greeting the customer
print("Welcome to our cafe")
print("pizza: RS40\npasta : Rs50\nburger : Rs60\ndessert : Rs30\ncoke : Rs20  \nwater : Rs10\njuice : Rs15\nTea : Rs15")

OrderTotal = 0
item1 = input("Enter the name of item you want :  ")
#to check item is in the menu or not
if item1 in menu:
    OrderTotal+= menu[item1] #here when the user inputs the item1 say its a pizza then the code will go to the menu dictionary and check the pizza value and will add it to the ordertotal which is initially 0
    print(f"Total price of {item1} is {menu[item1]}")
else :
    print(f"sorry {item1} not Available")

another_order = input("Anything else (yes/no) - ")
if another_order == "yes":
    item2 = input("Enter the item2 = ")
    if item2 in menu:
        OrderTotal+= menu[item2]
        print(f"Ordered item is {item2} is added successfully")
    else:
        print(f"sorry {item2} not Available")
print(f"Total amount  = {OrderTotal}")
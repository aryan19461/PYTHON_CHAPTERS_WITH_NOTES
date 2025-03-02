"""
List Uniqueness Checker
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]
"""
ListInput = input("List items are : ").split()
print(f"Orignal List is : {ListInput}")
for item in ListInput:
    if item in ListInput:
        print(f"Deplicate item is {item}\n")
        ListInput.remove(item)
        break

print(f"List after deletion is : {ListInput}")



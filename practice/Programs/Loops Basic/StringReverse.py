"""
Reverse a String
Problem: Reverse a string using a loop.
"""

string1 = input("Enter the string to reverse : ")
string2 = ""
for str in string1:
    string2 = str + string2

print(string2)
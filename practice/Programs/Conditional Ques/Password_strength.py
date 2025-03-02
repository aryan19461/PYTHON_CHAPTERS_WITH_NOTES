"""
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
"""

password = input("Enter the password: ")

if len(password) < 6:
    print("Password is too short")
elif 6 <= len(password) <= 10:
    print("Weak Password")
elif 11 <= len(password) <= 20:
    print("Strong Password")
elif len(password) >= 21:
    print("Very Strong Password")

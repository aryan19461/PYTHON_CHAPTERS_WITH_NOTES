import random

print("Welcome to Rock Scissor  paper game \n")
rps = ["🥊" , "✂️" , "🗞️" ]
user = input("Enter the choice (🥊/✂️/🗞️) = ")
cpu = random.choice(rps)
print(f"user shows {user} and cpu showed {cpu}\n")

if user ==cpu:
    print("It's a tie! 😂")
elif user == "🥊" :
    if cpu == "✂️" :
        print("user won")
    elif cpu == "🗞️":
        print("cpu won")
elif user == "🗞️" :
    if cpu == "✂️" :
        print("cpu won")
    elif cpu == "🥊":
        print("user won")
elif user == "🥊" :
    if cpu == "✂️" :
        print("user won")
    elif cpu == "🗞️":
        print("cpu won")

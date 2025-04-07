input_word = input("Enter the word : ")
reverse = input_word[::-1] # we are moving from reverse therefore -1 and star and end can be anything therefore ::

if(input_word == reverse ):
    print("palindrome detected")
else:
    print("not a palindrome")
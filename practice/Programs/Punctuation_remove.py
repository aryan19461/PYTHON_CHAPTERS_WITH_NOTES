input_string = input("Enter the Sentence: ")
punctuation = ''' !()-[]{};:"\,<>./!@#$%^&*~''' #not putting space in between otherwise space will also be treated as punctuation character
emptystring = ""
for i in input_string:
    if i not in punctuation:
        emptystring = emptystring + i

print(emptystring)
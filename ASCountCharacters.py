inputstring = input("Please enter any word(s)")
maxlength = int(len(inputstring))

print("The length of the string is: ", maxlength)

others=int(0)
uppercase=int(0)
lowercase=int(0)
numbers=int(0)
counter=int(0)

for counter in range (maxlength) :
    character = inputstring[counter]
    if ord(character) >= 33 and ord(character) <= 37:
        others = others + 1
    elif ord(character) >= 48 and ord(character) <= 57:
        numbers = numbers + 1
    elif ord(character) >= 65 and ord(character) <= 92:
        uppercase = uppercase + 1
    elif ord(character) >= 97 and ord(character) <= 123:
        lowercase = lowercase + 1
    else:
        others = others + 1

prompt1="The total for"
prompt2="are: "

print(prompt1, "symbols/spaces", prompt2, others)
print(prompt1, "uppercase letters", prompt2, uppercase)
print(prompt1, "lowercase leters", prompt2, lowercase)
print(prompt1, "numbers", prompt2, numbers)

# ord will turn your char into ascii code
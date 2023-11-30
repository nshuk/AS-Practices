inputstring = input("Please enter any word(s)")
maxlength = len(inputstring)
# use of len to count the length of the string

print("The length of the string is: ", maxlength)

# intialize the total of all values as 0
others = 0
uppercase = 0
lowercase = 0
numbers = 0
counter = 0

for counter in range (maxlength) :
    character = inputstring[counter] #[x] refers to the letter of the string at that index
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

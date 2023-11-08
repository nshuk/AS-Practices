smallestnum = int(input("Please input any number"))
count = 0
while count <= 9:
    num = int(input("Please input another number"))
    if num < smallestnum:
        smallestnum = num
    count = count + 1
print("The smallest number you've entered is", smallestnum)

#when i didn't put in the int datatype infront of both inputs of smallestnum and num, the num can't be assigned into num
#most probably because the num < smallestnum is not valid. it's only valid when they are int first.

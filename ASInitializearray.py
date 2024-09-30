List1 = [0 for i in range(7)] # value 0 

j = 0
for i in range (0,7):
    Num = int(input("Please input a number: "))
    List1[j] = Num
    j=j+1
print(List1)

#or

List2 = [] # empty list
for i in range (0,7):
    List2.append(int(input("Please enter num")))
print(List2)

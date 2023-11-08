i=int(0)
j=int(0)
List = [0 for i in range(7)]
for i in range (0,7):
    Num= int(input("Please input a number: "))
    List[j]=Num
    j=j+1
print(List)

#or

List2 = []
for i in range (0,7):
    List2.append(int(input("Please enter num")))
print(List2)
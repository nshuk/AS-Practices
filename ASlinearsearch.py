i=int(0)
j=int(0)
List = [0 for i in range(7)]
for i in range (0,7):
    Num= int(input("Please input a number: "))
    List[j]=Num
    j=j+1
print(List)

counter=int(0)
upperbound= len(List)
found = False
location = int(0)

searchv=int(input("Please input the search value: "))

while (found == False) and (counter<=upperbound) :
        if List[counter] == searchv:
            found = True
            location = counter
            print("The location is index ", location)
            counter = counter + 1
        else:
            counter = counter + 1
if found == False:
    print("Value not found")

#wtf pening
# condition tu kena AND baru betul. kalau OR salah. dia outofrange
# nak tukar post cond to pre cond kena tengok betul betul condition dia
# sebab condition dia patut reversed
# nak increment counter pun penting
# kalau post cond or, precond and
# kalau inequality pulak lebih kurang macam maths logicnya
# bool pulak False dengan True reversed
# generally selain tu = dengan !=. apa apa pun logik kena betul

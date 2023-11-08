runningtotal=int(0)
counter=int(1)
for counter in range (10):
    nextnum=int(input("Input a number"))
    runningtotal= runningtotal + nextnum
print(runningtotal)
average=float(runningtotal / 10)
print(average)
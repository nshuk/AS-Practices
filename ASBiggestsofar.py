biggestsofar=int(input("Input a number"))
counter=int(1)
for counter in range(10):
    nextnum=int(input("Input another number"))
    if nextnum > biggestsofar:
        biggestsofar = nextnum
print(biggestsofar)
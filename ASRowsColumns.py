nofrows=int(input("Input number of rows"))
nofcolumns=int(input("Input number of columns"))
symbol=input("Input any symbol")
rowcounter=int(1)
columncounter=int(1)
for rowcounter in range (nofrows):
    for colcounter in range (nofcolumns):
        print(symbol, end=" ")
    print(" ")

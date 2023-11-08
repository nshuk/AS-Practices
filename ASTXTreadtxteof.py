Filehandle = open("c:/9618/sampletext2.txt", "r")
Text = Filehandle.readline()
while len(Text)>0:
    print(Text)
    Text = Filehandle.readline()
Filehandle.close()



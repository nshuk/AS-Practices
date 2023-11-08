Filehandle = open("c:/9618/sampletext3.txt", "r")
Text = Filehandle.readline()
print("The student data that can be found inside the file:")
print(Text)
Student1 = Text
Filehandle.close()
print(" ")

Filehandle = open("c:/9618/sampletext3.txt", "a")
Student2 = "Hazni, 22.2, Professional Sciences"
Student3 = "Aimi, 22.8, Engineering"
newline = "\n"
Filehandle.write(newline)
Filehandle.write(Student2)
Filehandle.write(newline)
Filehandle.write(Student3)
Filehandle.close()

listname = [Student1, Student2, Student3]
print("The students' data after appended: ")
for row in listname:
    for index in row:
        print(index, end="")
    print("")
print(" ")

sorted_listname = sorted(listname)
print("The students' data after sorted: ")
for row in sorted_listname:
    for index in row:
        print(index, end="")
    print("")

#the sampletext3.txt should initially only include naqib's data. clear other students data to rerun.



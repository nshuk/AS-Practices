marks=input("Please enter your latest examination marks: ")
if int(marks) > 100 or int(marks) < 0:
    print("Invalid marks entered.") #validation method
elif int(marks) >= 80:
    grade="A"
    print("Here's your grade base on your marks: ", grade)
elif int(marks) >= 70:
    grade="B"
    print("Here's your grade base on your marks: ", grade)
elif int(marks) >= 60:
    grade="C"
    print("Here's your grade base on your marks: ", grade)
elif int(marks) >= 50:
    grade="D"
    print("Here's your grade base on your marks: ", grade)
elif int(marks) >= 40:
    grade="E"
    print("Here's your grade base on your marks: ", grade)
elif int(marks) >= 0:
    grade="Ungraded"
    print("Here's your grade base on your marks: ", grade)

#if you put a num out of the range, you wont get the output

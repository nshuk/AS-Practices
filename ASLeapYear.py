month=int(input("Please input the number of the month (1-12)"))
year=int(input("Please input the year"))
days=int(0)

if month == 2 and (year % 4 == 0) and (year % 100 > 0):
    days=29
    print(days)
elif month == 2:
    days=28
    print(days)
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
    days=31
    print(days)
elif month==4 or month==6 or month==9 or month==11 :
    days=30
    print(days)
else:
    print("Invalid month")

# the use of MOD in python is used with a symbol %
# MOD 4 means if the answer divided by 4 does not give any remainder, it means that
# it is perfectly divisible by 4




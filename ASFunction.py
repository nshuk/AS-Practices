def AreaofShapes():
    print("Calculate the are of different shapes")
    print("1. Triangle")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Quit")

def AreaTriangle():
    print("Enter the length of the: ")
    base= float(input("Base: "))
    height= float(input("Heigth: "))
    area=float(0.5*base*height)
    return area

def AreaCircle():
    print("Enter the radius of the circle: ")
    radius= float(input("Radius: "))
    area=float(3.14*radius*radius)
    return area

def AreaRectangle():
    print("Enter the length and width of the: ")
    length=float(input("Length: "))
    width=float(input("Width: "))
    area=float(length*width)
    return area

AreaofShapes()
choice = int(input("Please input your choice "))
if choice > 4 or choice < 1:
    print("Invalid choice")

if choice == 1:
    areaT=AreaTriangle()
    print("Area is: ", areaT)
elif choice == 2:
    areaC=AreaCircle()
    print("Area is: ", areaC)
elif choice == 3:
    areaR=AreaRectangle()
    print("Area is: ", areaR)
elif choice == 4:
    print("Thanks, bye.")

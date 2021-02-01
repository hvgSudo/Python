from turtle import *

def xy():
        print("\n1. Continue Drawing")
        print("2. Exit")
        c = int(input("Enter your choice: "))
        if c == 1:
            return 1
        else:
            return 0
        
def line():
    l = int(input("Enter the length of the line: "))
    n = int(input("Enter the angle to which the line is inclined to XY plane: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    setheading(n)
    forward(l)

def cir():
    r = int(input("\nEnter the radius of the circle: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    circle(r)

def rec():
    l = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the breadth of the rectangle: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(2):
        forward(l)
        left(90)
        forward(b)
        left(90)

def sq():
    s = int(input("Enter the side of the square: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(4):
        forward(s)
        left(90)
        
def tri():
    print("1. Iscosceles Triangle (angles = 45 45 90)")
    print("2. Right triangle (angles = 30 60 90)")
    l = int(input("Enter your choice: "))
    if l == 1:
        q = int(input("Enter the equal length: "))
        reset()
        forward(350)
        write('Y')
        backward(700)
        write('X')
        home()
        pensize(3)
        forward(q)
        left(90)
        forward(q)
        goto(0,0)
    elif l == 2:
        e = int(input("Enter the perpendicular length: "))
        r = int(input("Enter the base length: "))
        reset()
        forward(350)
        write('Y')
        backward(700)
        write('X')
        home()
        pensize(3)
        forward(r)
        left(90)
        forward(e)
        goto(0,0)
    else:
        print("Wrong choice")
       
def pen():
    p = int(input("Enter the side of the pentagon: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(5):
        forward(p)
        left(72)
        
def hexa():
    h = int(input("Enter the side of the hexagon: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(6):
        forward(h)
        left(60)
            
def hept():
    g = int(input("Enter the side of the heptagon: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(7):
        forward(g)
        left(51.42)
            
def octa():
    o = int(input("Enter the side of the octagon: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(8):
        forward(o)
        left(45)
            
def non():
    n = int(input("Enter the side of the nonagon: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(9):
        forward(n)
        left(40)
            
def dec():
    d = int(input("Enter the side of the decagon: "))
    reset()
    forward(350)
    write('Y')
    backward(700)
    write('X')
    home()
    pensize(3)
    for i in range(10):
        forward(d)
        left(36)
    
print("\n\t\t\tWELCOME TO DRAWING IN PYTHON\n")
print("\tHere you can draw polygons starting from a triangle to a decagon")
print("\t\t    You can also draw a line and a circle")
print("\t\t   The figures are drawn over the XY Plane")
print("\t\tThe XY Plane is nothing but a horizontal plane")
print("\t\t\tAll the diagrams are planes")
print("\t\tLine and circle have one point in the XY Plane")
print("\t\tThe other shapes have one edge in the XY Plane")
print("\t\t\tAll measurements are done in mm")
print("\n\n\t\t\t\tSo, Let's start")

while 1 == 1:
    print("\n1. Line")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Triangle")
    print("6. Pentagon")
    print("7. Hexagon")
    print("8. Heptagon")
    print("9. Octagon")
    print("10. Nonagon")
    print("11. Decagon")
    print("12. Exit")
    a = input("Enter your choice: ")
    try:
        a = int(a)
    except:
        print("\nWrong input. Only numbers accepted")
        continue
    print("\n")
     
    if a == 1:
        line()
        e = xy()
        if e != 1:
            break
         
    elif a == 2:
        cir()
        e = xy()
        if e != 1:
            break
        
    elif a == 3:
        rec()
        e = xy()
        if e != 1:
            break
        
    elif a == 4:
        sq()
        e = xy()
        if e != 1:
            break

    elif a == 5:
        tri()
        e = xy()
        if e != 1:
            break
            
    elif a == 6:
        pen()
        e = xy()
        if e != 1:
            break
        
    elif a == 7:
        hexa()
        e = xy()
        if e != 1:
            break
        
    elif a == 8:
        hept()
        e = xy()
        if e != 1:
            break

    elif a == 9:
        octa()
        e = xy()
        if e != 1:
            break

    elif a == 10:
        non()
        e = xy()
        if e != 1:
            break

    elif a == 11:
        dec()
        e = xy()
        if e != 1:
            break

    elif a == 12:
        break

    else:
        print("Wrong input")

print("\n\t\t\tThank You for drawing")

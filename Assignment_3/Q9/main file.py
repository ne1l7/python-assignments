import shapes

print("Choose shape: 1.Circle 2.Rectangle 3.Triangle")
ch = input("Enter choice: ")

if ch == "1":
    r = float(input("Radius: "))
    result = shapes.area_circle(r)
    print("Area of circle:", result)

elif ch == "2":
    l = float(input("Length: "))
    b = float(input("Breadth: "))
    result = shapes.area_rectangle(l, b)
    print("Area of rectangle:", result)

elif ch == "3":
    b = float(input("Base: "))
    h = float(input("Height: "))
    result = shapes.area_triangle(b, h)
    print("Area of triangle:", result)

else:
    print("Invalid choice")
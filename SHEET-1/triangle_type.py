a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    if 90 in [a, b, c]:
        print("Right triangle")
    elif max(a, b, c) > 90:
        print("Obtuse triangle")
    else:
        print("Acute triangle")
else:
    print("Not a valid triangle")
  

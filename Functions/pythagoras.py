print("1. Find Hypotenuse")
print("2. Find one side")
choice = int(input())
if choice == 1:
    a = float(input())
    b = float(input())
    c = (a**2 + b**2) ** 0.5
    print(c)
elif choice == 2:
    c = float(input())
    a = float(input())
    b = (c**2 - a**2) ** 0.5
    print(b)
else:
    print("Invalid")
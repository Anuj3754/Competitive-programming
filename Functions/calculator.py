print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input())
num1 = float(input())
num2 = float(input())
if choice == 1:
    result = num1 + num2
    print(result)
elif choice == 2:
    result = num1 - num2
    print(result)
elif choice == 3:
    result = num1 * num2
    print(result)
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Error")
else:
    print("Invalid")
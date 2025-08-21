percent = int(input("enter percentage: "))

if percent < 25:
    grade = "D"
elif percent < 45:
    grade = "C"
elif percent < 65:
    grade = "B"
elif percent < 85:
    grade = "A"
else:
    grade = "A+"

print("Grade:", grade)

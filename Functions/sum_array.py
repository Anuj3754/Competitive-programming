N = int(input())
A = []
for i in range(N):
    num = int(input())
    A.append(num)
total = 0
for num in A:
    total += num
print(total)
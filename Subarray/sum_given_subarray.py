N = int(input())
arr = list(map(int, input().split()))
L, R = map(int, input().split())
total = 0
for i in range(L - 1, R):
    total += arr[i]
print(total)
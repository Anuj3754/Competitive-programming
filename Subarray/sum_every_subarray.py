N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    total = 0
    for j in range(i, N):
        total += arr[j]
        print(total)
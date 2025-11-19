N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    for j in range(i, N):
        for k in range(i, j + 1):
            print(arr[k], end=" ")
        print()
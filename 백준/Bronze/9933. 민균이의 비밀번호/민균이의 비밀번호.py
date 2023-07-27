import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]

for i in range(N - 1):
    for j in range(i, N):
        if arr[i][::-1] == arr[j]:
            print(len(arr[i]), arr[i][len(arr[i]) // 2])
            exit()
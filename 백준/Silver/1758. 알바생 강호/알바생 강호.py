n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
cnt=0
for i in range(n):
    cnt+= max(arr[i] - i,0)

print(cnt)
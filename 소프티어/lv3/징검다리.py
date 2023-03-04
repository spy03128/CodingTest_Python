import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [1]*n

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
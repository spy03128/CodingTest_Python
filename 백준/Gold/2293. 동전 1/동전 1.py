import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for c in coin:
    for x in range(1, k + 1):
        if x - c >= 0:
            dp[x] += dp[x - c]

print(dp[k])
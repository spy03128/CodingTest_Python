import sys
input = sys.stdin.readline

c, n = map(int, input().split())
dp = [1000000] * 2001
dp[0] = 0
array = []

for _ in range(n):
    cost, customer = map(int, input().split())
    array.append((cost, customer))

for x in range(1, 2001):
    for co, cu in array:
        if x - cu >= 0:
            dp[x] = min(dp[x], dp[x - cu] + co)

print(min(dp[c:]))
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * 100001

    for coin in coins:
        dp[coin] += 1
        for j in range(coin, m + 1):
            dp[j] = max(dp[j], dp[j]+ dp[j - coin])
    print(dp[m])
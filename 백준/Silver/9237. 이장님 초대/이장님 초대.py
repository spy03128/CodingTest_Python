n = int(input())
day = list(map(int, input().split()))

day.sort(reverse=True)

max_day = day[0]

if n == 1:
    print(n + 2)
else:
    for i in range(1, n):
        if max_day < (i + day[i]):
            max_day = i + day[i]

    result = max_day + 2
    print(result)


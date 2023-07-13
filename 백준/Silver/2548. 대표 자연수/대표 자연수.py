N = int(input())
li = list(map(int, input().split()))

li.sort()

if N %2 == 0:
    print(li[N // 2 - 1])

else:
    print(li[N // 2])
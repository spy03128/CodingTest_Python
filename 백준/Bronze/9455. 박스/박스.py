import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m,n = map(int, input().split())
    arr = [[] for _ in range(n)]

    for i in range(m):
        a = list(input().split())
        for j in range(n):
            arr[j].append(a[j])

    cnt = 0
    for i in range(n):
        num = arr[i].count('1')
        ground = m -1

        for j in range(m-1,-1,-1):
            if arr[i][j] =='1':
                cnt +=ground-j
                ground-=1

    print(cnt)
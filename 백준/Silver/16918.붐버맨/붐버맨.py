from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
r,c,n = map(int,input().split())
arr = [list(input()) for _ in range(r)]
arr2 = [['.']*c for _ in range(r)]
arr3 = [['.']*c for _ in range(r)]
check= [[0]*c for _ in range(r)]
check2= [[0]*c for _ in range(r)]

Q = deque()

for i in range(r):
    for j in range(c):
        if arr[i][j]=='O':
            Q.append((i,j))

while Q:
    now = Q.popleft()
    arr2[now[0]][now[1]]='.'
    check[now[0]][now[1]]=1
    for i in range(4):
        x = now[0]+dx[i]
        y = now[1]+dy[i]
        if 0<=x<r and 0<=y<c:
            arr2[x][y]='.'
            check[x][y]=1
for i in range(r):
    for j in range(c):
        if check[i][j]==0:
            arr2[i][j]='O'

if n==1:
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end="")
        print()
elif n!=1 and n%4==1:
    for i in range(r):
        for j in range(c):
            if arr2[i][j] == 'O':
                Q.append((i, j))

    while Q:
        now = Q.popleft()
        arr3[now[0]][now[1]] = '.'
        check2[now[0]][now[1]] = 1
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0 <= x < r and 0 <= y < c:
                arr3[x][y] = '.'
                check2[x][y] = 1

    for i in range(r):
        for j in range(c):
            if check2[i][j] == 0:
                arr3[i][j] = 'O'
    for i in range(r):
        for j in range(c):
            print(arr3[i][j], end="")
        print()
elif n%4==3:
    for i in range(r):
        for j in range(c):
            print(arr2[i][j], end="")
        print()
else:
    for i in range(r):
        for j in range(c):
            print('O', end="")
        print()


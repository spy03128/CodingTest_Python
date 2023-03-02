from collections import deque

def BFS():

    while Q:
        now = Q.popleft()
        for i in arr[now]:
          if check[i]==0:
                check[i]=now
                Q.append(i)


Q = deque()
n = int(input())
arr = [[] for _ in range(n+1)]
check = [0]*(n+1)
for _ in range(n-1):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)


Q.append(1)
check[1]=1
BFS()

for i in range(2,n+1):
    print(check[i])
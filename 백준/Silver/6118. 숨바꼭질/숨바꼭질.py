from collections import deque
def BFS():
    while Q:
        now = Q.popleft()
        for i in arr[now]:
            if visited[i]==0:
                dp[i] = dp[now]+1
                visited[i]=1
                Q.append(i)


Q = deque()
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
dp = [0]*(n+1)
visited = [0]*(n+1)

for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
Q.append(1)
visited[1]=1

BFS()
maxlist = []
maxim = max(dp)
for i in range(n+1):
    if dp[i]==maxim:
        maxlist.append(i)
maxlist.sort()
print("%d %d %d" %(maxlist[0], maxim, len(maxlist)))
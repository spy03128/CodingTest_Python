from collections import deque
import sys

def BFS(i):
    global cnt,visited,check
    # print(flag)
    Q.append(i)
    while Q:
        now = Q.popleft()
        # print(now,start)
        if (not flag) and now == end:
            visited[now]=now
            x = check[now]
            while True:
                if x == check[x]:
                    Q.clear()
                    break
                else:
                    # print("여기")

                    visited[x] = 1
                    x = check[x]
                    cnt += 1
            return

        if flag and now == start:
            x = visited[now]
            while True:
                if x == visited[x]:
                    break
                else:
                    # print("걸림")

                    x = visited[x]
                    cnt += 1
            return

        for i in arr[now]:
            if flag:
                if visited[i]==0:
                    Q.append(i)
                    visited[i]=now
            else:
                if check[i] == 0:
                    Q.append(i)
                    check[i] = now


Q = deque()
n,m = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
check = [0]*(n+1)
visited = [0]*(n+1)
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

for i in range(n+1):
    arr[i].sort()

start,end = map(int,sys.stdin.readline().split())
check[start] = start
cnt = 2
flag = False
BFS(start)
flag = True
BFS(end)
print(cnt)


"""
10 13
1 2
1 3
2 4
2 5
3 4
3 10
4 6
4 7
5 6
6 8
7 8
7 9
9 10
1 8
"""
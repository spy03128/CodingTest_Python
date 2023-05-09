import sys
from collections import deque
input = sys.stdin.readline
def change_direction(s):
    global direction
    if s=="L":
        if direction==0:
            direction=3
        else:
            direction-=1
    elif s=="D":
        if direction==3:
            direction=0
        else:
            direction+=1

def BFS():
    global S
    visited[0][0] = 1
    S.append((0,0))
    Q = deque()
    Q.append((0,0))
    sec = -1
    c_sec_idx = 0
    while Q:
        sec+=1
        c_sec = (directions[c_sec_idx])[0]
        c_dir = (directions[c_sec_idx])[1]
        x,y = Q.popleft()
        if c_sec==sec:
            change_direction(c_dir)
            if c_sec_idx < len(directions)-1:
                c_sec_idx+=1
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
            #사과 여부 확인
            S.insert(0, (nx, ny))
            visited[nx][ny] = 1

            if arr[nx][ny] == 1:
                arr[nx][ny]=0
            else:
                i,j = S.pop()
                visited[i][j]=0

            Q.append((nx,ny))

        else:
            #벽이나 몸에 닿이면 게임끝
            print(sec+1)

            exit()


dx = [-1,0,1,0]
dy = [0,1,0,-1]
N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
directions = []
direction = 1
S = deque()

for _ in range(K):
    x,y = map(int,input().split())
    x,y = x-1, y-1
    arr[x][y]=1
D = int(input())
for _ in range(D):
    t,c = input().split()
    directions.append((int(t),c))

BFS()
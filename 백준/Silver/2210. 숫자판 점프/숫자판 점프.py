def DFS(i,j,str):
    if len(str)==6:
        res.add(str)
        return
    for x in range(4):
        nx = i +dx[x]
        ny = j +dy[x]
        if 0<=nx<5 and 0<=ny<5:
            DFS(nx,ny,str+arr[nx][ny])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

arr = [list(map(str, input().split())) for _ in range(5)]
res = set()
for i in range(5):
    for j in range(5):
        DFS(i,j,arr[i][j])

print(len(res))
def DFS(L):
    global res
    if L == n:
        tmp = 0
        for x,y in arr:
            if x<=0:
                tmp+=1
        res = max(tmp,res)
        return

    if arr[L][0]<=0 or all(x[0]<=0 for idx, x in enumerate(arr) if idx!=L) :
        DFS(L+1)
        return
    f1,g1 = arr[L]
    for i in range(n):
        if arr[i][0] <= 0 or i==L:
            continue
        f2,g2 = arr[i]
        arr[L], arr[i] = (f1-g2, g1), (f2-g1, g2)
        DFS(L+1)
        arr[L], arr[i] = (f1, g1), (f2, g2)

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
res = 0
DFS(0)
print(res)

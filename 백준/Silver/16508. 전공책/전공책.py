import sys
input = sys.stdin.readline


def DFS(v):
    global minX
    if v == n:
        alpha = [0]*26
        res = 0
        for i in range(n):
            if check[i]==1:
                res += int(book[i][0])
                for x in book[i][1]:
                    alpha[ord(x)-65]+=1

        for i in T.strip():
            if alpha[ord(i)-65] == 0:
                return
            else:
                alpha[ord(i)-65]-=1
        minX = min(minX, res)
        return

    check[v] = 1
    DFS(v+1)
    check[v] = 0
    DFS(v+1)

T = input()
n = int(input())
book = [list(input().split()) for _ in range(n)]
check = [0] * n
minX = 1000000000
DFS(0)
if minX==1000000000:
    print(-1)
else: print(minX)
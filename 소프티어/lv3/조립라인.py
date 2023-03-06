import sys
n = int(sys.stdin.readline())
arrA=list()
arrB=list()
dpA=[0]*n
dpB=[0]*n
for _ in range(n-1):
    a,b,ab,ba = map(int,sys.stdin.readline().split())
    arrA.append((a,ab))
    arrB.append((b,ba))
aend,bend = map(int,sys.stdin.readline().split())
arrA.append((aend,0))
arrB.append((bend,0))

for i in range(n):
    if i==0:
        dpA[i]=arrA[0][0]
        dpB[i]=arrB[0][0]
    else:
        dpA[i] = min(dpA[i-1], dpB[i-1]+arrB[i-1][1]) + arrA[i][0]
        dpB[i] = min(dpB[i-1], dpA[i-1]+arrA[i-1][1]) + arrB[i][0]

print(min(dpA[n-1],dpB[n-1]))
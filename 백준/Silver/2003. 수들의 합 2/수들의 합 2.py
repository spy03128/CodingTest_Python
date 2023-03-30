import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
s,e,cnt=0,0,0
total = arr[0]
while s<=e:
    if s==e and arr[s]>m:
        e+=1
        if e==n:
            break
        total+=arr[e]
    if total<=m:
        if total==m:
            cnt+=1
        e+=1
        if e==n:
            break
        total+=arr[e]
    elif total>m:
        total-=arr[s]
        s+=1
print(cnt)
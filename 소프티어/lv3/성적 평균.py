import sys

n,k = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
for _ in range(k):
    s,e = map(int,sys.stdin.readline().split())
    print("{:.2f}".format(round(sum(arr[s-1:e])/(e-s+1),2)))
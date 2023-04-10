import sys
from collections import Counter

input = sys.stdin.readline

n=int(input())
arr = []
for _ in range(n):
    s = input().rstrip().split(".")
    arr.append(s[1])
res = Counter(arr)
res = sorted(res.items())

for x in res:
    print(x[0],x[1])
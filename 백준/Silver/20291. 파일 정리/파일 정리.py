import sys
from collections import Counter

input = sys.stdin.readline

n=int(input())
arr = []
for _ in range(n):
    s = input().rstrip()
    for i in range(len(s)):
        if s[i]=='.':
            arr.append(s[i+1:])
res = Counter(arr)
res = sorted(res.items())
for x in res:
    print(x[0],x[1])
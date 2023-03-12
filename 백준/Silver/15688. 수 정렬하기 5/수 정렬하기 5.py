import sys

n = int(input())
m = []
for _ in range(n):
    m.append(int(sys.stdin.readline()))
for i in sorted(m):
    print(i)
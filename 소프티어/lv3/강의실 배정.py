import sys
import heapq as hq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    hq.heappush(q,(e,s))


cnt, end = 0, 0
while q:
    e,s = hq.heappop(q)
    if s >= end:
        cnt+=1
        end = e
print(cnt)
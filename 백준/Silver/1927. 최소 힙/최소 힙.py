import heapq as hq
import sys
heap =[]
n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap, x)

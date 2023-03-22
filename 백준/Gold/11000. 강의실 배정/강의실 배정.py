import heapq as hq
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    hq.heappush(arr,(s,e))
time = []
hq.heappush(time,hq.heappop(arr)[1])
while arr:
    s,e = hq.heappop(arr)

    if time[0] > s:
        hq.heappush(time,e)
    else:
        hq.heappop(time)
        hq.heappush(time,e)

print(len(time))


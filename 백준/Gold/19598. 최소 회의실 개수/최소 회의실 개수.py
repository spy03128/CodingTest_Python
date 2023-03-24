import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    s,e = map(int,input().split())
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
import sys
input = sys.stdin.readline
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
array.sort(key=lambda x: (x[0], -x[1]))
sc = [[0]*366 for _ in range(N)]
maxim, min_len, max_len, total = 0, array[0][0], array[0][1], 0
for s,e in array:
    idx = 0
    min_len = min(min_len, s)

    if s > max_len + 1:
        total += (max_len - min_len + 1) * (maxim+1)
        min_len = s
        maxim = 0
    for i in range(N):
        if sc[i][s] == 0:
            idx = i
            break
    for i in range(s, e+1):
        sc[idx][i] = 1
    maxim = max(maxim, idx)
    max_len = max(max_len, e)

total += (max_len - min_len + 1) * (maxim + 1)

print(total)
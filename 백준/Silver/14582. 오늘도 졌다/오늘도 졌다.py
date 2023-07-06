import sys
input = sys.stdin.readline

g = list(map(int, input().strip().split()))
st = list(map(int, input().strip().split()))

g_sum, s_sum, flag = 0, 0, False

for i in range(9):
    g_sum += g[i]
    if g_sum > s_sum:
        flag = True
    s_sum += st[i]
    
print("Yes" if g_sum < s_sum and flag else "No")
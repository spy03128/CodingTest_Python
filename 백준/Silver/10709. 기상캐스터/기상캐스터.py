h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
s_ = [[0] * w for i in range(h)]
ac = False
num = 1
for i in range(h):
    for j in range(w):
        if ac == False and s[i][j] == '.':
            s_[i][j] = -1
        elif s[i][j] == 'c':
            ac = True
            num = 1
        else:
            s_[i][j] = num
            num += 1
    ac = False
    num = 1
for i in range(h):
    for j in range(w):
        print(s_[i][j], end=' ')
    print()
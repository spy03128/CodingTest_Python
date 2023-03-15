dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    arr = [list(input()) for i in range(r)]

    answer = []
    for i in range(r):
        temp = []
        for j in range(c):
            cnt = 0
            if arr[i][j] == "*":
                temp.append("*")
            else:
                for k in range(8):
                    a = i + dx[k]
                    b = j + dy[k]
                    if 0 <= a <= r - 1 and 0 <= b <= c - 1:
                        if arr[a][b] == "*":
                            cnt += 1
                temp.append(str(cnt))
        answer.append(temp)

    for i in answer:
        print("".join(i))

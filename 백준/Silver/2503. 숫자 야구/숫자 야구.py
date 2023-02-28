from itertools import permutations
arr = list(permutations([1,2,3,4,5,6,7,8,9],3))

n = int(input())
num = [list(input().split()) for _ in range(n)]
cnt = 0
for i in arr:
    tmp = str(i[0]) + str(i[1]) + str(i[2])
    for j in num:
        s, b = 0, 0

        for x in range(3):
            if j[0][x] == str(i[x]):
                s+=1
            else:
                if j[0][x] in tmp:
                    b+=1
        if s!=int(j[1]) or b!=int(j[2]):
            break
    else:
        cnt+=1

print(cnt)
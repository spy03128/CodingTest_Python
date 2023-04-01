import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

alpha = [[0] * 8 for _ in range(26)]
for x in arr:
    for i in range(len(x)):
        alpha[ord(x[i])-65][i+(8-len(x))] += 1

for x in alpha:
    for i in range(len(x)):
        if x[i]>=10:
            x[i-1]+=x[i]//10
            x[i]=x[i]%10

res = []
for x in alpha:
    tmp = int("".join(map(str,x)))
    if tmp !=0:
        res.append(tmp)

res.sort(reverse=True)
s = 9
total = 0
for x in range(len(res)):
    total += res[x]*s
    s-=1

print(total)
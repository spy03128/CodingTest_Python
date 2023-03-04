import sys
n,m = map(int,sys.stdin.readline().split())
meter = [0]*n
speed = [0]*n
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if i == 0:
        meter[i] =x
    else:   
        meter[i] = meter[i-1] + x
    speed[i] =y

maxim = 0
meter2 = [0]*m
speed2 = [0]*m
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    if i == 0:
        meter2[i] =x
    else:   
        meter2[i] = meter2[i-1] + x
    speed2[i] =y

a, b= 0,0
while(True):
    tmp = speed2[b]-speed[a]
    maxim=max(maxim,tmp)
    if meter[a]==100 and meter2[b]==100:
        break
    if meter[a]<meter2[b]:
        a+=1
    elif meter[a]>meter2[b]:
        b+=1
    else:
        a+=1
        b+=1
    

print(maxim)
import sys
input = sys.stdin.readline

count = [0] * (1000 + 1) 

cnt = 0 
for _ in range(10):
    num = int(input())
    cnt += num 
    count[num] += 1  

print(cnt // 10) 
print(count.index(max(count)))
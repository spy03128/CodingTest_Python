import sys
input = sys.stdin.readline

L = int(input())
nums = list(map(int, input().split()))
n = int(input())

nums.sort() 
if n in nums:
    print(0)
else:
    min = 0
    max = 0
    for num in nums:       
        if num < n:     
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1                  
    min += 1
    print((n-min)*(max-n+1) + (max-n))
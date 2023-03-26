N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for num in range(1,N+1):
    x,y,xsize,ysize = map(int,input().split())
    for x_idx, X in enumerate(arr):
        for y_idx, Y in enumerate(X):
            if x <= x_idx <= x+xsize-1 and y <= y_idx <= y+ysize-1:
                arr[x_idx][y_idx] = num

for num in range(1,N+1):
    sum = 0
    for k in arr:
        for j in k :
            if j == num :
                sum+=1
    print(sum)
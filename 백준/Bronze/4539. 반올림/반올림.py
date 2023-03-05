n = int(input())

for _ in range(n):
    arr = list(input())
    for i in range(len(arr)-1,0,-1):
        if int(arr[i])>=5:
            arr[i-1]=str(int(arr[i-1])+1)
        arr[i] = '0'
    for j in range(len(arr)):
        print(arr[j], end=" ")
    print()
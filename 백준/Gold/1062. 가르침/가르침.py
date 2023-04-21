import sys,re
from itertools import combinations
input = sys.stdin.readline

n,k = map(int,input().split())
tmp = "antic"
arr = [input().rstrip()[4:-4] for _ in range(n)]
res = 0

if k < 5:
    print(res)
else:
    alpha = ["b","d","e","f","g","h","j","k","l","m","o","p","q","r","s","u","v","w","x","y","z"]
    result = 0
    num = k - 5
    for x in combinations(alpha,num):
        st = "".join(x)
        st+="antic"
        cnt = 0
        for i in range(len(arr)):
            for j in arr[i]:
                if j not in st:
                    break
            else:
                cnt+=1
        result = max(result,cnt)


    print(result)
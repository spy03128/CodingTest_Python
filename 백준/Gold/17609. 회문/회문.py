import sys

input = sys.stdin.readline

n=int(input())
for _ in range(n):
    res = 2
    str = input().rstrip()

    if str == str[::-1]:
        res = 0
    else:
        s,e=0,len(str)-1
        check = 0
        while s<=e:
            if check>1:
                break

            if str[s]==str[e]:
                s+=1
                e-=1
            else:
                if str[s+1:e+1] == str[e:s:-1]:
                    res=1
                elif str[s:e] == (str[e-1:s-1:-1] if s > 0 else str[e-1::-1]):
                    res=1

                break


    print(res)

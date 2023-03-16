n=int(input())

for i in range(n):
    k=int(input())
    tmp=[int(input()) for j in range(k)]

    cnt=tmp.count(max(tmp))
    maxim=max(tmp)
    flag= max(tmp) > sum(tmp)/2
    
    if flag==1:
        result='majority'
    else : 
        result='minority'
    if cnt!=1: 
        print("no winner")
    else :
        print("%s winner %d" %(result,tmp.index(maxim)+1))
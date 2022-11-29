def solution(k, tangerine):
    answer = 0
    
    tangerine.sort()
    x = tangerine[0]
    list = []
    num = 0
    for i in tangerine:
        if x == i:
            num+=1
        else:
            list.append(num)
            x = i
            num = 1
    list.append(num)
    list.sort(reverse=True)
    if(list[0]>=k): return 1
    sum,result = 0,0
    for i in list:
        sum+=i
        result+=1
        if sum >= k: return result

    
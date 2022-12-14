from collections import Counter

def solution(want, number, discount):
    result = 0
    want_count = {}
    for i in range(0,len(want)):
        want_count[want[i]] = number[i]
    
    
    leng = sum(number)
    count = Counter(discount[0:leng])

    idx = 0

    while leng <= len(discount):
        flag = False
        for key, value in want_count.items():
            if(count[key] < value):
                flag = True
                break
        
        #값이 모자라면 넘어가고 값이 크면 result + 1
        if(not flag):
            result += 1
            
        if leng == len(discount):
            break

        count[discount[idx]]-=1
        count[discount[leng]]+=1
        idx+=1
        leng+=1
        
    return result
m = int(input())
money = list(map(int,input().split()))

jun, jun_m , seong, seong_m = 0, m, 0 ,m
for i in range(14):
    if jun_m <money[i]:
        continue
    jun+= jun_m//money[i]
    jun_m = jun_m%money[i]

for i in range(3,14):
    if money[i-3]<money[i-2]<money[i-1] and seong!=0:
        #전량 매도
        seong_m += seong * money[i]
        seong = 0

    elif money[i - 3] > money[i - 2] > money[i-1]:
        # 전량 매수
        if seong_m < money[i]:
            continue
        seong+= seong_m//money[i]
        seong_m = seong_m%money[i]


jun_m+= (jun*money[13])
seong_m+= (seong*money[13])

if jun_m>seong_m:
    print("BNP")
elif jun_m<seong_m:
    print("TIMING")
else:
    print("SAMESAME")

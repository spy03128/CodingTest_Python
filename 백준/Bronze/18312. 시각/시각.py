n, k = map(int, input().split())

time = set()
def fun(x):
    if x<10:
        return "0" + str(x)
    else:
        return str(x)

for i in range(n+1):
    yy = fun(i)
    for j in range(60):
        mm =  fun(j)
        for h in range(60):
            dd = fun(h)
            t = yy + mm + dd
            if str(k) in t:
                time.add(t)
print(len(time))
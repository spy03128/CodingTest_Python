n = int(input())

def sumf(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sumf(x), x))
for i in arr:
    print(i)
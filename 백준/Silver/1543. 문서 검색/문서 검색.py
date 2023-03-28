a = input()
b = input()
cnt, n = 0, 0

while n <= len(a) - len(b):
    if a[n:n + len(b)] == b:
        cnt += 1
        n += len(b)
    else:
        n += 1
print(cnt)
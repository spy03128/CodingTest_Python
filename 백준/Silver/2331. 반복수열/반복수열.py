n, m = map(int, input().split())
cur = n
nums = [cur]

while True:
    temp = str(cur)
    num = 0
    for i in temp:
        num += int(i) ** m
    if num in nums:
        nums = nums[:nums.index(num)]
        break
    else:
        nums.append(num)
        cur = num

print(len(nums))
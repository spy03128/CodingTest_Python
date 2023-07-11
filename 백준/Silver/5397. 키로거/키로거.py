n = int(input())

for _ in range(n):
    left = []
    right = []
    L = input()
    
    for i in L:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    
    print(''.join(left))
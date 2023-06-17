import sys
from itertools import permutations
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    arr = [input().rstrip() for _ in range(k)]
    result = list(permutations(arr, 2))
    for word in result:
        w = word[0] + word[1]
        for i in range(len(w)//2):
            if w[i] != w[len(w) - 1 - i]:
                break
        else:
            print(w)
            break
    else:
        print(0)
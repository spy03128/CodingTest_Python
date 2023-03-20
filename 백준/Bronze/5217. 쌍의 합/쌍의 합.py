for _ in range(int(input())):
    n = int(input())
    s = 1
    print("Pairs for %d:" % n, end=' ')

    for k in range((n - 1) // 2):
        if k != 0:
            print(',', end=' ')
        print(s, n - s, end='')
        s += 1

    print()
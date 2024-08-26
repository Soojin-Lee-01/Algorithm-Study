import sys

N, M = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split(' ')))

for i in range(M):
    a, b, c,  = map(int, sys.stdin.readline().split(' '))
    if a == 1:
        data[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            if data[j] == 0:
                data[j] = 1
            else:
                data[j] = 0
    elif a == 3:
        for j in range(b-1, c):
            data[j] = 0
    else:
        for j in range(b-1, c):
            data[j] = 1
print(' '.join(map(str, data)))


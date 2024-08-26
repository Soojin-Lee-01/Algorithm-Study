import sys

n, q = map(int, sys.stdin.readline().split(' '))

visited = [0] * (n + 1)

for i in range(q):
    num = int(sys.stdin.readline())
    target = num
    ground = 0

    while target != 1: # 루트에 도착 할 때까지!
        if visited[target] >= 1:
            ground = target

        target //= 2

    if ground:
        print(ground)
    else:
        visited[num] = 1
        print(0)









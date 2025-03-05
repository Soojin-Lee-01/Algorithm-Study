"""
공간 메모리

1MB = 1024바이트 x 1024바이트

"""
N = int(input())

mem = [0] * (N+1)
prev = [0] * (N+1)
def dp(n):
    for i in range(2, N+1):
        mem[i] = mem[i-1] + 1
        prev[i] = i - 1
        if i % 2 == 0:
            if mem[i] > mem[i//2] + 1:
                mem[i] = mem[i//2] + 1
                prev[i] = i // 2
        if i % 3 == 0:
            if mem[i] > mem[i//3] + 1:
                mem[i] = mem[i // 3] + 1
                prev[i] = i // 3

    print(mem[n])

    path = []
    while n != 0:
        path.append(n)
        n = prev[n]

    print(' '.join(map(str, path)))

dp(N)

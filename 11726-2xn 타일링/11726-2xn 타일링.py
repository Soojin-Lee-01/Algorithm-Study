import sys

n = int(sys.stdin.readline())

mem = {}
def dp(n):
    mem[1] = 1
    mem[2] = 2
    mem[3] = 3
    if n in mem:
        return mem[n] % 10007
    else:
        for i in range(4, n + 1):
            mem[i] = dp(i-1) + dp(i-2)
    return mem[n] % 10007

print(dp(n))

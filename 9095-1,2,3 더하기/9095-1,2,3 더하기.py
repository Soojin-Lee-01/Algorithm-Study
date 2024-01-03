import sys

test = int(sys.stdin.readline())

mem = {}
mem[1] = 1
mem[2] = 2
mem[3] = 4
def dp(n):
    if n in mem:
        return mem[n]
    else:
        for j in range(4, n+1):
            mem[j] = mem[j-1] + mem[j-2] + mem[j-3]
    return mem[n]

for i in range(test):
    a = int(sys.stdin.readline())
    print(dp(a))
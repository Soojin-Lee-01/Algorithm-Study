import sys

n, m = map(int, sys.stdin.readline().split(' '))

mem = {}

dp = 1

for i in range(1, n+1):
    dp *= i
    mem[i] = dp

mem[n] = dp

result = mem[n] // (mem[n-m] * mem[m])

print(result)


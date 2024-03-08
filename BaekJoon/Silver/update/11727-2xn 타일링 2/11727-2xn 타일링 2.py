import sys

n = int(sys.stdin.readline())

mem = [0] * 1001
mem[1] = 1
mem[2] = 3

for i in range(3, n+1):
    mem[i] = mem[i-1] + (mem[i-2] * 2)

print(mem[n] % 10007)
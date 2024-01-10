import sys

n = int(sys.stdin.readline())

mem = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]

for i in range(10, n+1):
    mem.append(mem[i-5] + 1)

print(mem[n])



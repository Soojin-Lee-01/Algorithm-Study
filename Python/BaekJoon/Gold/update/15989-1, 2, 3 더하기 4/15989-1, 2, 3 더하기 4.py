n = int(input())

mem = {}
for i in range(10001):
    mem[i] = 1

for i in range(2, 10001):
    mem[i] += mem[i-2]

for i in range(3, 10001):
    mem[i] += mem[i-3]

for i in range(n):
    num = int(input())
    print(mem[num])

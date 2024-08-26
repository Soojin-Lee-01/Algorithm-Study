import sys

num = int(sys.stdin.readline())

word = list(map(int, sys.stdin.readline().rstrip().split(' ')))

mem = [1 for _ in range(num)]

for i in range(1, num):
    for j in range(0, i):
        if word[j] < word[i]:
            mem[i] = max(mem[i], mem[j] + 1)

print(max(mem))






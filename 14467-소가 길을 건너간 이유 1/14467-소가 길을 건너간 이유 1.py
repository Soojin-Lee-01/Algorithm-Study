import sys

count = 0

cow = {}

for i in range(10):
    cow[i+1] = []

N = int(sys.stdin.readline())

for i in range(N):
    a, b = map(int ,sys.stdin.readline().split(' '))
    if cow[a] == []:
        cow[a] = b
    elif cow[a] != [] and cow[a] != b:
        count += 1
        cow[a] = b

print(count)

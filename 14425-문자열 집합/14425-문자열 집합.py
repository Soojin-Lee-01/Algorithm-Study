import sys

n, m = map(int, sys.stdin.readline().split(' '))

word = {}

for i in range(n):
    word[i+1] = []

for i in range(n):
    data = sys.stdin.readline().rstrip()
    word[i+1] = data

count = 0

temp = {v:k for k, v in word.items()}

for _ in range(m):
    data = sys.stdin.readline().rstrip()
    if data in temp:
        count += 1

print(count)


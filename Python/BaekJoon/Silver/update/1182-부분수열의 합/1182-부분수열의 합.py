import sys

n, m = map(int, sys.stdin.readline().split(' '))

data = list(map(int, sys.stdin.readline().split(' ')))

count = 0
def back(s, start = 0, combo = []):
    global count
    if len(combo) == s:
        if sum(combo) == m:
            count += 1
    for i in range(start, len(data)):
        combo.append(data[i])
        back(s, i+1, combo)
        combo.pop()

for i in range(len(data)):
    back(i+1)

print(count)
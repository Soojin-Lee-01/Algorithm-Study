import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rstrip()))

result = 0

for i in data:
    result += i

print(result)
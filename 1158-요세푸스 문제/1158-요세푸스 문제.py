import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

circle = deque()

result = []

for i in range(N):
    circle.append(i+1)

while circle:
    circle.rotate(-(K-1))
    result.append(circle.popleft())

print("<" + ', '.join(map(str, result)) + ">")


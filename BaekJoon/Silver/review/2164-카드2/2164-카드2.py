import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([i + 1 for i in range(N)])

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)

print(''.join(map(str, queue)))

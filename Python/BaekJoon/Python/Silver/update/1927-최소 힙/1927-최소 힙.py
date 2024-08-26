import heapq
import sys

num = int(sys.stdin.readline())

data = []

for i in range(num):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(data, n)
    else:
        if (len(data)) > 0:
            print(heapq.heappop(data))
        else:
            print(0)


import sys
from heapq import heapify, heappop, heappush

n = int(sys.stdin.readline())

heap = []
heap = [i * -1 for i in heap]

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if len(heap) > 0:
            weight = heappop(heap)
            print(-1 * weight)
        else:
            print(0)
    elif a != 0:
        heappush(heap, a * -1)






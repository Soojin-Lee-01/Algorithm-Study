import sys
from heapq import heapify, heappop, heappush

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    datas = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    for data in datas:
        if len(heap) < n:
            heappush(heap, data)
        else:
            if heap[0] < data:
                heappop(heap)
                heappush(heap, data)

print(heap[0])






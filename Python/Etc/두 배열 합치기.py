"""
1. 단순히 배열을 합치고 정렬하면 O(nlogn) 시간복잡도가 걸린다.
2. 하지만 two pointer로 이를 해결하면 O(n) 시간복잡도가 걸린다.
"""

import sys

N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
data2 = list(map(int, sys.stdin.readline().split()))

p1, p2 = 0, 0

answer = []

while(p1 < N and p2 < M):
    if data[p1] < data2[p2]:
        answer.append(data[p1])
        p1 += 1
    else:
        answer.append(data2[p2])
        p2 += 1

while(p1 < N):
    answer.append(data[p1])
    p1 += 1

while(p2 < M):
    answer.append(data2[p2])
    p2 += 1

print(' '.join(map(str, answer)))

import sys
from collections import deque

data = list(sys.stdin.readline().rstrip())

queue = deque()

count = 0

for i in range(len(data)):
    if data[i] == "(":
        queue.append(i)
    else:
        if data[i-1] == "(":
            queue.popleft()
            count += len(queue)
        else:
            queue.popleft()
            count += 1

print(count)



"""
stack 이용!
() 발견하면 그전에 쌓아놓은 (만큼 +
) 발견하면  +1

예상 시간 복잡도 : O(n)
"""

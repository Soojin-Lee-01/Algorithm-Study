import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split(' '))
q = deque()
n = 0
q2 = []
for i in range(a):
    q.append(i+1)

while q:
    for j in range(b-1):
        q.append(q.popleft())
    q2.append(q.popleft())

print("<" + str(q2).strip("[]")+ ">") # 문자열로 변환하고 []를 제거!
import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
"""
enumerate() 함수?
-> enumerate(iterable, startIndex)
iterable : 반복할 수 있는 개체
startIndex : 선택사항, 지정하지 않으면 0 / 지정하면 그 숫자부터 증가!
"""

for i in range(N):
    p = deq.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        deq.rotate(-(p[1] - 1))
    else:
        deq.rotate(-p[1])

"""
** 리스트 회전 문제는 deque 자료형을 사용 **
- 리스트 자료형을 deque 자료형으로 바꾼 후 rotate() 함수를 이용하여 회전!
- 음수 -> 왼쪽 회전 / 양수 -> 오른쪽 회전
"""




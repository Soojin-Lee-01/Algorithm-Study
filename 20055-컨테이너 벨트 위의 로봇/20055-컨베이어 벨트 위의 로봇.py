import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

data = map(int, sys.stdin.readline().rstrip().split())

queue = deque(data)
up = 0 # 단계수
robot = deque(0 for _ in range(n))

while True:
    up += 1

    # 컨베이어 벨트 회전
    queue.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0

    # 로봇 이동
    for i in range(n-2, -1, -1): # 가장 먼저 벨트에 올라간 로봇부터
        if queue[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            queue[i+1] -= 1
    robot[-1] = 0

    # 올리는 위치에 로봇을 올린다
    if queue[0] != 0 and robot[0] != 1:
        robot[0] = 1
        queue[0] -=1

    # 내구도 확인
    if queue.count(0) >= k:
        break

print(up)








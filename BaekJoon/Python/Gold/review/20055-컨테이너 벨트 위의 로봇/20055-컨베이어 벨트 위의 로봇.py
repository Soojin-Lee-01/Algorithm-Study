from collections import deque

n, k = map(int, input().split())
data = deque(map(int, input().split()))
# 로봇이 올려져있는지 확인
robot = deque([0] * n)

# 각 단계
count = 0

while True:
    # 단계 +1
    count += 1
    # 한칸 회전
    data.rotate(1)
    # 만약에 로봇이 내리는 위치에 있다면 내리기
    robot[-1] = 0
    # 로봇도 같이 회전
    robot.rotate(1)
    # 만약에 로봇이 내리는 위치에 있다면 내리기
    robot[-1] = 0

    # 처음 올린것부터 위치 이동
    for i in range(n-2, -1, -1):
        # 만약에 다음 칸의 내구성이 0 이상이고, 로봇이 없다면 올린다.
        if data[i+1] > 0 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] =1
            robot[i] = 0
            data[i+1] -= 1
    # 로봇이 내리는 위치에 있다면 내리기
    robot[-1] = 0

    # 만약에 올리는 위치에 내구성이 0 이상이고, 로봇이 없다면 올리기
    if data[0] > 0 and robot[0] != 1:
        robot[0] = 1
        data[0] -= 1

    # 만약에 내구성이 0 인것이 k개 이상이면 종료
    if data.count(0) >= k:
        break


print(count)
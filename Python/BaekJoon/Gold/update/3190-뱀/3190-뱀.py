from collections import deque

n = int(input())
k = int(input())

# 뱀이 움직이는 그래프
graph = [[0 for _ in range(n)] for _ in range(n)]

# 사과가 있는 위치 2로 표시
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

# 방향이 얼마나 바뀌는지
l = int(input())

# 방향 바뀌는 정보 담기
data = {}

for i in range(l):
    x, c = map(str, input().split())
    data[int(x)] = c

# 방향 : 우, 아래, 좌, 위
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 현재의 방향
cur_d = 0

# sneak 몸 위치 정보
sneak = deque()

# 최초에는 0, 0에 위치
sneak.append((0, 0))

# 뱀의 최초 위치
r = 0
c = 0

# 초 카운트
count = 0

while True:
    count += 1

    # 뱀 이동
    r += directions[cur_d][0]
    c += directions[cur_d][1]

    # 만약에 뱀이 벽에 안부딪히면
    if 0 <= r < n and 0 <= c < n:
        # 만약에 몸이 부딪히면 종료
        if (r, c) in sneak:
            break
        # 그게 아니라면 뱀 몸 정보 담기
        sneak.append((r, c))
    # 만약에 벽에 부딪히면 종료
    else:
        break

    # 만약에 사과가 있다면
    if graph[r][c] == 2:
        # 사과를 먹는다
        graph[r][c] = 0

    # 만약에 사과가 없다면, 몸의 길이는 바뀌지 않는다.
    else:
        sneak.popleft()

    # 만약에 방향이 바뀌어야 한다면
    if count in data:
        if data[count] == "L":
            cur_d = (cur_d - 1) % 4
        elif data[count] == "D":
            cur_d = (cur_d + 1) % 4

print(count)
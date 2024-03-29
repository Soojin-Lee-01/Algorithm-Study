import sys
from collections import deque

# 입력 받기
r, c, t = map(int, sys.stdin.readline().split())

graph = []
for _ in range(r):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 미세먼지 확산 함수 정의
def spread_dust():
    spread = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                count = 0
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < r and 0 <= nj < c and graph[ni][nj] != -1:
                        spread[ni][nj] += graph[i][j] // 5
                        count += 1
                graph[i][j] -= (graph[i][j] // 5) * count

    for i in range(r):
        for j in range(c):
            graph[i][j] += spread[i][j]

# 공기청정기 작동 함수 정의
def operate_air_cleaner():
    # 위쪽 공기청정기 작동
    for i in range(air_cleaner_pos[0] - 2, -1, -1):
        graph[i + 1][0] = graph[i][0]
    for j in range(1, c):
        graph[0][j - 1] = graph[0][j]
    for i in range(1, air_cleaner_pos[0] + 1):
        graph[i - 1][c - 1] = graph[i][c - 1]
    for j in range(c - 2, 0, -1):
        graph[air_cleaner_pos[0]][j + 1] = graph[air_cleaner_pos[0]][j]
    graph[air_cleaner_pos[0]][1] = 0

    # 아래쪽 공기청정기 작동
    for i in range(air_cleaner_pos[1] + 2, r):
        graph[i - 1][0] = graph[i][0]
    for j in range(1, c):
        graph[r - 1][j - 1] = graph[r - 1][j]
    for i in range(r - 2, air_cleaner_pos[1] - 1, -1):
        graph[i + 1][c - 1] = graph[i][c - 1]
    for j in range(c - 2, 0, -1):
        graph[air_cleaner_pos[1]][j + 1] = graph[air_cleaner_pos[1]][j]
    graph[air_cleaner_pos[1]][1] = 0

# 공기청정기 위치 찾기
air_cleaner_pos = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            air_cleaner_pos.append(i)

# t초 동안 반복
for _ in range(t):
    spread_dust()
    operate_air_cleaner()

# 미세먼지 총합 구하기
total_dust = sum(sum(row) for row in graph) + 2  # 공기청정기가 -1을 차지하므로 +2

# 결과 출력
print(total_dust)

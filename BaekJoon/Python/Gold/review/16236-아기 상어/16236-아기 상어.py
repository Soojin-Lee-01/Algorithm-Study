"""
시간복잡도를 위해서 bfs 함수안에서 먹을 물고기를 지정하자!
"""

from collections import deque

N = int(input())
graph = []

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

# 초기 상어 크기, 먹은 물고기 갯수, 위치
shrak_size = 2
eat = 0
r, c = 0, 0

# 상어의 초기 위치를 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            r = i
            c = j
            graph[i][j] = 0  # 상어가 있는 위치를 0으로 초기화

# 먹을 수 있는 물고기 리스트를 반환하는 함수
def can():
    temp = []
    for i in range(N):
        for j in range(N):
            if 0 < graph[i][j] < shrak_size:  # 상어가 먹을 수 있는 물고기만 추가
                temp.append((i, j))
    return temp

# BFS를 사용해 가장 가까운 물고기를 찾는 함수
def bfs(r, c, eat):
    queue = deque()
    queue.append((r, c, 0))
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    da = []

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()

        # 먹을 수 있는 물고기를 찾으면 리스트에 추가
        if (cur_r, cur_c) in eat:
            da.append((cur_len, cur_r, cur_c))

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c] and graph[next_r][next_c] <= shrak_size:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True

    if da:
        # 가장 가까운 물고기를 거리, 행, 열 순으로 정렬하여 반환
        da.sort(key=lambda x: (x[0], x[1], x[2]))
        return da[0]  # 가장 가까운 거리 -> 행 -> 열 순으로 따져서 먹을 물고기 정보 반환

    return None  # 먹을 수 있는 물고기가 없는 경우

time = 0

while True:
    eat_data = can()  # 먹을 수 있는 물고기 리스트 가져오기
    # 먹을 수 있는 물고기 없으면 끝
    if len(eat_data) == 0:
        print(time)
        break

    fish = bfs(r, c, eat_data)
    if not fish:  # 먹을 물고기가 없으면 종료
        print(time)
        break

    # 상어를 물고기 위치로 이동시키기
    r, c = fish[1], fish[2]
    time += fish[0]  # 이동한 거리만큼 시간을 더해줌
    graph[r][c] = 0  # 물고기를 먹었으니 해당 위치를 0으로 변경

    eat += 1

    # 상어 크기만큼 물고기를 먹으면 크기를 증가
    if eat == shrak_size:
        shrak_size += 1
        eat = 0

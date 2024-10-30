"""
시간 복잡도를 생각해보자!
O(N * M * 4)
N, M 최대 : 300

300 * 300 * 4 = 360000
"""
from collections import deque

N, M = map(int, input().split())
graph = []

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

answer = 0

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0<= next_c < M:
                if not visited[next_r][next_c]:
                    if graph[next_r][next_c] != 0:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True


while True:

    check = 0
    for a in range(len(graph)):
        check += graph[a].count(0)

    if check == (N * M):
        print(0)
        break

    temp_graph = [[0 for _ in range(M)] for _ in range(N)]
    # 1. 먼저 상,하,좌,우 빈공간을 탐색한다.
    for a in range(len(graph)):
        for b in range(len(graph[0])):
            if graph[a][b] != 0:
                count = 0
                for dr, dc in directions:
                    next_r = a + dr
                    next_c = b + dc
                    if graph[next_r][next_c] == 0:
                        count += 1
                temp_graph[a][b] = count

    # 2. 빙하가 녹는다.
    for a in range(len(temp_graph)):
        for b in range(len(temp_graph[0])):
            if temp_graph[a][b] > 0:
                graph[a][b] -= temp_graph[a][b]
                if graph[a][b] < 0:
                    graph[a][b] = 0

    # 3. 빙하가 두 덩어리인지 확인한다.
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    area = 0
    for a in range(len(graph)):
        for b in range(len(graph[0])):
            if graph[a][b] != 0 and not visited[a][b]:
                bfs(a, b)
                area += 1

    answer += 1

    if area > 1:
        print(answer)
        break

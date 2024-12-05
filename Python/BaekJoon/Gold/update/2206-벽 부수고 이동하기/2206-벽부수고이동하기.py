from collections import deque

N, M = map(int, input().split())

graph = []

data = []

# 그래프 구성
for _ in range(N):
    row = list(map(int, input()))
    graph.append(row)

# 벽 담기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            data.append((i, j))

# 최단 거리 구하는 함수
def bfs(r, c):

    queue = deque()
    queue.append((r, c, 0, 0))

    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    visited[r][c][0] = True
    visited[r][c][1] = True

    # 상, 하, 좌, 우
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c, breaklable, dist = queue.popleft()


        if cur_r == N-1 and cur_c == M-1:
            return dist + 1

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < M:
                if not visited[next_r][next_c][breaklable]:
                    if graph[next_r][next_c] == 0:
                        visited[next_r][next_c][breaklable] = True
                        queue.append((next_r, next_c, breaklable, dist + 1))
                    else:
                        if breaklable == 0:
                            visited[next_r][next_c][breaklable] = True
                            queue.append((next_r, next_c, 1, dist+1))

    return -1

answer = bfs(0, 0)

print(answer)

from collections import deque

N, M = map(int, input().split())

# 그래프 구성
graph = []

for _ in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

virus = []
wall = []

# 바이러스 위치와 벽 위치 담기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 1:
            wall.append((i, j))

com = []

# 조합으로 모든 경우의 수 담기
def combinations(n, start = 0, combo = []):
    if len(combo) == n:
        com.append(combo[:])
        return

    for k in range(start, len(virus)):
        combo.append(virus[k])
        combinations(n, k+1, combo)
        combo.pop()


# 그래프 탐색
def bfs(dat):
    queue = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for x, y in dat:
        queue.append((x, y))
        visited[x][y] = 0

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    now_time = 0

    while queue:
        cur_r, cur_c = queue.popleft()
        cur_time = visited[cur_r][cur_c]

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                # 방문하지 않았거나, 벽이 아닐때 방문
                if visited[next_r][next_c] == -1 and graph[next_r][next_c] != 1:
                    visited[next_r][next_c] = cur_time + 1
                    queue.append((next_r, next_c))
                    # 빈칸일때 시간 업데이트
                    if graph[next_r][next_c] == 0:
                        now_time = visited[next_r][next_c]

    # 만약 다 방문하지 못하면 무한대 반환
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and visited[i][j] == -1:
                return float('inf')

    # 다 방문했다면 완료 시간 반환
    return now_time

# 만약 빈칸이 없다면 0을 출력
if len(virus) + len(wall) == N**2:
    print(0)
else:
    combinations(M)
    # 양의 무한대
    final = float('inf')

    for temp in com:
        time = bfs(temp)
        final = min(time, final)

    if final == float('inf'):
        print(-1)
    else:
        print(final)

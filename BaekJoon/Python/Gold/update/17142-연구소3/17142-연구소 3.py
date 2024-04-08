from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

combinations = []
def combination(n, start=0, combo=[]):
    if len(combo) == n:
        combinations.append(combo[:])
        return
    for i in range(start, len(virus)):
        combo.append(virus[i])
        combination(n, i+1, combo)
        combo.pop()

combination(M)

def bfs(virus_locs):
    queue = deque(virus_locs)
    visited = [[False]*N for _ in range(N)]
    for x, y, z in virus_locs:
        visited[x][y] = True
    max_time = 0

    while queue:
        x, y, time = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, time+1))
                if graph[nx][ny] == 0:
                    max_time = max(max_time, time+1)

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] == 0:
                return float('inf')
    return max_time

result = float('inf')
for combo in combinations:
    combo_with_time = [(x, y, 0) for x, y in combo]
    result = min(result, bfs(combo_with_time))

if result == float('inf'):
    print(-1)
else:
    print(result)

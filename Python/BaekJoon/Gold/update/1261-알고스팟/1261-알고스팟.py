from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(M):
    data = list(map(int, input().strip()))
    graph.append(data)

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    visited = [[-1] * N for _ in range(M)]
    visited[0][0] = 0

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < len(graph) and 0 <= next_c < len(graph[0]):
                if visited[next_r][next_c] == -1:
                    if graph[next_r][next_c] == 0:
                        queue.appendleft((next_r, next_c))
                        visited[next_r][next_c] = visited[cur_r][cur_c]
                    else:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = visited[cur_r][cur_c] + 1

    return visited[M-1][N-1]

print(bfs(0, 0))

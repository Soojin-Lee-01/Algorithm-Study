import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(data)

visited = [[False] * n for _ in range(n)]
count = 0


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    groud = 1
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < n and 0 <= next_c < n:
                if graph[next_r][next_c] == 1:
                    if visited[next_r][next_c] is False:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        groud += 1
    return groud


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] is False:
            result.append(bfs(i, j))
            count += 1

result = sorted(result)

print(count)
for i in result:
    print(i)


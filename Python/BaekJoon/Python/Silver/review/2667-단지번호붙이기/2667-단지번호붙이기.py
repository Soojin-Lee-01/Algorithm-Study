import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(data)
result = []
def apart(grid):
    visited = [[False] * N for _ in range(N)]
    def bfs(r,c):
        groud = 1
        row_len = len(grid)
        col_len = len(grid[0])
        visited[r][c] = True
        queue = deque()
        queue.append((r, c))
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if (next_r >= 0 and next_r < row_len) and (next_c >= 0 and next_c < col_len):
                    if grid[next_r][next_c] == 1:
                        if not visited[next_r][next_c]:
                            queue.append((next_r, next_c))
                            visited[next_r][next_c] = True
                            groud += 1

        return groud

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                result.append(bfs(i, j))
apart(graph)

count = 0
for i in result:
    if i != 0:
        count += 1

print(count)
result.sort()
for i in result:
    if i != 0:
        print(i)
import sys
from collections import deque

n , m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]
result_grid = [[-1] * m for _ in range(n)]


def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0))
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True

    while queue:
        cur_r, cur_c , cur_dist = queue.popleft()
        directions= [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if next_r >= 0 and next_r < len(grid) and next_c >= 0 and next_c < len(grid[0]):
                if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_dist + 1))
                    visited[next_r][next_c] = True
                    result_grid[next_r][next_c] = cur_dist + 1
a = 0
b = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            a = i
            b = j
        elif grid[i][j] == 0:
            result_grid[i][j] = 0
result_grid[a][b] = 0

bfs(a, b)

for i in range(n):
    for j in range(m):
        print(result_grid[i][j], end=' ')
    print()

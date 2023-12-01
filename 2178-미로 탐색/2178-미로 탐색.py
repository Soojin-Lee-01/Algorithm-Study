import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(data)

def bfs(grid, r, c):
    distance = -1
    queue = deque()
    queue.append((r,c,1))

    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    visited[r][c] = True

    # 출발지와 목적지를 건너갈 수 없을때는 -1을 return
    if grid[0][0] == 0 or grid[row_len-1][col_len-1] == 0:
        return -1

    while queue:
        cur_r, cur_c, cur_dist = queue.popleft()
        # 목적지에 도달했을 때 distance return
        if cur_r == row_len - 1 and cur_c == col_len - 1:
            return cur_dist
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if (next_r >= 0 and next_r < row_len) and (next_c >= 0 and next_c < col_len):
                if grid[next_r][next_c] == 1:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_dist+1))
                        visited[next_r][next_c] = True

    return distance


print(bfs(graph, 0, 0))

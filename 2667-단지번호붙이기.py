from collections import deque
import sys

n = int(sys.stdin.readline())

grid = [list(map(int, input())) for _ in range(n)]

def numLands(grid):
    list = []
    row = len(grid)
    col = len(grid)
    visited = [[False] * col for _ in range(row)]

    def bfs(r,c):
        count = 1
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        visited[r][c] = True
        queue = deque()
        queue.append((r,c))

        while queue:
            cur_r, cur_c = queue.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                    if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c))
                        count += 1
        list.append(count)

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    a = sorted(list)
    print(len(list))
    for i in a:
        print(i)

numLands(grid)




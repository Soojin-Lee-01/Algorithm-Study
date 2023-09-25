from collections import deque

def Maze(n, m, grid):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0, 1))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, distance = queue.popleft()
        if x == n - 1 and y == m - 1:
            return distance
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and  nx < n and ny >= 0 and ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return -1


n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]

result = Maze(n, m , grid)
print(result)
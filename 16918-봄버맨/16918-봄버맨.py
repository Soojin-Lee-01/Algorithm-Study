import sys

R, C, N = map(int, sys.stdin.readline().split())

grid = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
bomp_grid = [['O'] * C for _ in range(R)]

# 폭탄 터트리기
def bfs(grid):
    current_grid = [['O' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                current_grid[i][j] = '.'
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    next_r = i + dr
                    next_c = j + dc
                    if next_r >= 0 and next_r < R and next_c >= 0 and next_c < C:
                        current_grid[next_r][next_c] = '.'

    return current_grid

# 초기
if N == 1:
    for i in range(R):
        for j in range(C):
            print(grid[i][j], end='')
        print()
# 폭탄 모두 설치
elif N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print("O", end='')
        print()
# 폭탄 터짐
elif N % 4 == 3:
    result_grid = bfs(grid)
    for i in range(R):
        for j in range(C):
            print(result_grid[i][j], end='')
        print()
# 폭탄 터지고 또 터짐
elif N % 4 == 1:
    result_grid = bfs(grid)
    result_grid = bfs(result_grid)
    for i in range(R):
        for j in range(C):
            print(result_grid[i][j], end='')
        print()


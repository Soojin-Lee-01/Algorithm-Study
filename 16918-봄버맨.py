import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().rstrip().split())

grid = []

for i in range(R):
    grid.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()

def bfs(queue, grid): # 폭탄을 모두 터트린다.
    while queue:
        x, y = queue.popleft()
        grid[x][y] = '.'
        for i in range(4):
            next_x, next_y = x + dx[i] , y + dy[i]
            if next_x >= 0 and next_x < R and next_y >= 0 and next_y < C and grid[next_x][next_y] == "O":
                grid[next_x][next_y] = '.'


def main(t):
    global queue, grid
    if t == 1:
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "O":
                    queue.append((i, j)) # 초기 폭탄 상태를 기록

    elif t % 2 == 1:
        bfs(queue, grid) # 폭탄을 모두 폭발
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'O':
                    queue.append((i, j))

    else:
        grid = [['O'] * C for _ in range(R)]


for i in range(1, N+1):
    main(i)

for i in grid:
    print(''.join(i))

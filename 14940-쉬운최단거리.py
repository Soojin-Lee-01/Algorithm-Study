import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [[] * N for _ in range(M)]

for i in range(N):
    data = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph[i] = data

visited = [[-1] * M for _ in range(N)] # -1로 초기화

def bfs(r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    queue = deque()
    queue.append((r,c))
    visited[r][c] = 0 # 방문표시

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if (next_r >= 0 and next_r < N) and (next_c >= 0 and next_c < M):
                if graph[next_r][next_c] == 1:
                    if visited[next_r][next_c] == -1:
                        visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                        queue.append((next_r, next_c))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2 and visited[i][j] == -1: # 2이며 방문하지 않았을때 bfs 수행
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()





import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))

graph = []
for i in range(n):
    data = list(map(int , sys.stdin.readline().rstrip()))
    graph.append(data)
visited = [[False] * m for _ in range(n)]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < n and next_c >= 0 and next_c < m:
                if graph[next_r][next_c] == 0:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True

result = []
check = 0
for i in range(m):
    if graph[0][i] == 0:
        bfs(0, i)

for i in range(m):
    if visited[n-1][i] == True:
        print("YES")
        check = -1
        break

if check != -1:
    print("NO")



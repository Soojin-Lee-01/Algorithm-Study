import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split(' '))

graph = []

for i in range(n):
    data = list(map(int, sys.stdin.readline().rsplit(' ')))
    graph.append(data)

def bfs(store):
    directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    for k, s in store:
        queue.append((k, s, 0))
        visited[k][s] = True
    short = 0
    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        short = cur_len
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if (0 <= next_r < n and 0 <= next_c < m):
                if not visited[next_r][next_c]:
                    if graph[next_r][next_c] == 0:
                        graph[next_r][next_c] = 1
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c, cur_len + 1))

    return short

store = set()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            store.add((i, j))

result = bfs(store)
check = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            check = -1
            exit()
if check == 0:
    print(result)





from collections import deque
import copy

n = int(input())

graph = []
temp_graph = []

for i in range(n):
    data = list(map(str, input().rstrip()))
    graph.append(data)

temp_graph = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if temp_graph[i][j] == 'G':
            temp_graph[i][j] = 'R'


def bfs(visi, gra, r, c, color):
    queue = deque()
    queue.append((r, c))
    visi[r][c] = True
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < n and 0 <= next_c < n:
                if not visi[next_r][next_c]:
                    if gra[next_r][next_c] == color:
                        queue.append((next_r, next_c))
                        visi[next_r][next_c] = True


visited1 = [[False for _ in range(n)] for _ in range(n)]
visited2 = [[False for _ in range(n)] for _ in range(n)]
result = [0, 0]

# 적록색약이 아닐 때
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            if not visited1[i][j]:
                bfs(visited1, graph, i, j, 'R')
                result[0] += 1
        elif graph[i][j] == 'G':
            if not visited1[i][j]:
                bfs(visited1, graph, i, j, 'G')
                result[0] += 1
        elif graph[i][j] == 'B':
            if not visited1[i][j]:
                bfs(visited1, graph, i, j, 'B')
                result[0] += 1

# 적록색약일 때
for i in range(n):
    for j in range(n):
        if temp_graph[i][j] == 'R':
            if not visited2[i][j]:
                bfs(visited2, temp_graph, i, j, 'R')
                result[1] += 1
        elif temp_graph[i][j] == 'B':
            if not visited2[i][j]:
                bfs(visited2, temp_graph, i, j, 'B')
                result[1] += 1

print(' '.join(map(str, result)))
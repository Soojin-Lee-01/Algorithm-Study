import copy
from collections import deque

num = int(input())
graph = []

for i in range(num):
    data = list(map(str, input().rstrip()))
    graph.append(data)

temp = copy.deepcopy(graph)

for i in range(num):
    for j in range(num):
        if temp[i][j] == 'R':
            temp[i][j] = 'G'

visited = [[False for _ in range(num)] for _ in range(num)]
visited2 = [[False for _ in range(num)] for _ in range(num)]

def bfs(r, c, gra, color, vi):
    queue = deque()
    queue.append((r, c))
    vi[r][c] = True
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < num and 0 <= next_c < num:
                if not vi[next_r][next_c] and gra[next_r][next_c] == color:
                    queue.append((next_r, next_c))
                    vi[next_r][next_c] = True
count = 0
count1 = 0
for i in range(num):
    for j in range(num):
        if not visited[i][j]:
            bfs(i, j, graph, graph[i][j], visited)
            count += 1

for i in range(num):
    for j in range(num):
        if not visited2[i][j]:
            bfs(i, j, temp, temp[i][j], visited2)
            count1 += 1

print(count, count1)

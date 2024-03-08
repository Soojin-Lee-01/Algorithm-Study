import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [] # 원래 그래프

for i in range(n):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)

open_graph = []

for i in range(n):
    data = list(map(str, sys.stdin.readline().rstrip()))
    open_graph.append(data)


def bfs(r, c):
    queue = deque()
    count = 0
    queue.append((r, c))
    directions = [(-1,0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < len(graph) and next_c >= 0 and next_c < len(graph[0]):
                if graph[next_r][next_c] == "*":
                    count += 1

    return  count

result = [["." for _ in range(n)] for _ in range(n)]

result_count = 0
for i in range(n):
    for j in range(n):
        if open_graph[i][j] == "x" and graph[i][j] != "*":
            result[i][j] = bfs(i,j)
for i in range(n):
    for j in range(n):
        if graph[i][j] == "*" and open_graph[i][j] == "x":
            result_count = 1
if result_count == 1:
    for i in range(n):
        for j in range(n):
            if open_graph[i][j] == "x" and graph[i][j] != "*":
                graph[i][j] = bfs(i, j)
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end='')
        print()
else:
    for i in range(n):
        for j in range(n):
            print(result[i][j], end='')
        print()




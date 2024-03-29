import sys
from collections import deque

def bfs(r, c, map):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < len(map) and next_c >= 0 and next_c < len(map[0]):
                if visited[next_r][next_c] is False and map[next_r][next_c] == 1:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))

while True:
    w, h = map(int, sys.stdin.readline().split(' '))
    if w == 0 and h == 0:
        break
    else:
        count = 0
        graph = []
        for i in range(h):
            data = list(map(int, sys.stdin.readline().rstrip().split(' ')))
            graph.append(data)
        visited = [[False] * w for _ in range(h)]
        for j in range(len(graph)):
            for k in range(len(graph[0])):
                if graph[j][k] == 1 and not visited[j][k]:
                    bfs(j, k, graph)
                    count += 1
        print(count)


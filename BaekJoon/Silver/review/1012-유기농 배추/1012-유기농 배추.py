import sys
from collections import deque

test = int(sys.stdin.readline())

def bfs(r, c, grap, visi):
    queue = deque()
    queue.append((r, c))
    visi[r][c] = True

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < len(graph)and next_c >= 0 and next_c < len(graph[0]):
                if grap[next_r][next_c] == 1:
                    if visi[next_r][next_c] is False:
                        queue.append((next_r, next_c))
                        visi[next_r][next_c] = True
result = []
for i in range(test):
    count = 0
    m, n, number = map(int, sys.stdin.readline().rstrip().split(' '))

    graph = [[0 for _ in range(m)] for _ in range(n)]

    visited = [[False for _ in range(m)] for _ in range(n)]

    for j in range(number):
        a, b = map(int, sys.stdin.readline().rstrip().split(' '))
        graph[b][a] = 1

    for k in range(n):
        for l in range(m):
            if graph[k][l] == 1 and not visited[k][l]:
                count += 1
                bfs(k, l, graph, visited)
    result.append(count)


for i in result:
    print(i)
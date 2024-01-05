import sys
from collections import deque

test = int(sys.stdin.readline())

def bfs(r, c, grap, visi):
    visi[r][c] = True
    queue = deque()
    queue.append((r, c))
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < len(graph)and next_c >= 0 and next_c < len(graph[0]):
                if grap[next_r][next_c] == 1 and visi[next_r][next_c] is not True:
                    queue.append((next_r, next_c))
                    visi[next_r][next_c] = True


result = []
for i in range(test):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split(' '))
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split(' '))
        graph[b][a] = 1
    for a in range(len(graph)):
        for b in range(len(graph[0])):
            if graph[a][b] == 1 and not visited[a][b]:
                bfs(a, b, graph, visited)
                count += 1
    result.append(count)

for i in result:
    print(i)






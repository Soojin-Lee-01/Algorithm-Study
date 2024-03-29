import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = {}

for i in range(N):
    graph[i+1] = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

visited_dfs = []
def dfs(start_v):
    visited_dfs.append(start_v)
    for v in graph[start_v]:
        if v not in visited_dfs:
            dfs(v)
    return ' '.join(map(str, visited_dfs))

print(dfs(V))

visited_bfs = []
def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    visited_bfs.append(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited_bfs:
                visited_bfs.append(v)
                queue.append(v)

    return ' '.join(map(str,visited_bfs))

print(bfs(V))

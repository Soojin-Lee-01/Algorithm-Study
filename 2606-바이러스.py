import sys
from collections import deque

n = int(sys.stdin.readline())
e = int(sys.stdin.readline())
graph = {}

for i in range(n):
    graph[i + 1] = []

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # 양방향 그래프
    graph[b].append(a)


# bfs
def bfs(graph, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    print(len(visited) - 1) # 자기 자신 제외


bfs(graph, 1)
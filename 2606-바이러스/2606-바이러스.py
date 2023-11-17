import sys
from collections import deque

com = int(sys.stdin.readline())
network = int(sys.stdin.readline())

graph = {}

for i in range(com):
    graph[i+1] = []

for i in range(network):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    visited = [start_v]
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return len(visited) - 1

print(bfs(1))



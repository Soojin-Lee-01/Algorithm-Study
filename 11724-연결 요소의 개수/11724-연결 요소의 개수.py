import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))

graph = {}

for i in range(n):
    graph[i+1] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]

def bfs(start_v):
    queue = deque()
    visited[start_v] = True
    queue.append(start_v)

    while queue:
        cur_r = queue.popleft()
        for v in graph[cur_r]:
            if visited[v] is False:
                queue.append(v)
                visited[v] = True

count = 0
for i in graph:
    if visited[i] is False:
        bfs(i)
        count += 1
print(count)



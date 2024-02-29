import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(' '))
s, e = map(int, sys.stdin.readline().split(' '))

graph = {}
for i in range(n):
    graph[i+1] = []
    if i == 0:
        graph[i+1].append(2)
    elif i > 0 and i < n-1:
        graph[i+1].append(i)
        graph[i+1].append(i+2)
    elif i == n-1:
        graph[i+1].append(i)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split(' '))
    graph[x].append(y)
    graph[y].append(x)


def bfs(start_v, end):
    count = 0
    queue = deque()
    queue.append((start_v, count))
    visited = [False] * (n+1)
    visited[start_v] = True

    while queue:
        cur_v, route = queue.popleft()
        if cur_v == end:
            return route
        for v in graph[cur_v]:
            if visited[v] is not True:
                queue.append((v, route+1))
                visited[v] = True

    return count

print(bfs(s, e))







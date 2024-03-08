import sys
from collections import deque

graph = {}

num = int(sys.stdin.readline())

for i in range(num):
    graph[i+1] = []

first, end = map(int, sys.stdin.readline().split(' '))

route = int(sys.stdin.readline())

for i in range(route):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)


def bfs(first, end):
    queue = deque()
    queue.append((first, 0))
    visited = [False] * (num+1)
    visited[first] = True

    while queue:
        cur_v, cnt = queue.popleft()
        if cur_v == end:
            return cnt
        for v in graph[cur_v]:
            if visited[v] is False:
                queue.append((v, cnt + 1))
                visited[v] = True

answer = bfs(first, end)
if answer is not None:
    print(answer)
else:
    print(-1)

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = {}

for i in range(N):
    graph[i+1] = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

result = {}
for i in range(N):
    result[i+1] = []

def result1(graph):
    count = 0
    def bfs(start_v, count):
        visited = [False] * (N + 1)
        visited[start_v] = True
        queue = deque()
        queue.append(start_v)
        count = 1
        while queue:
            cur_v = queue.popleft()
            for v in graph[cur_v]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    count += 1

        return count

    for i in range(N):
        a = bfs(i+1, count)
        result[i+1].append(a)

result1(graph)
print(result)
max = 0
for i in result:
    if result[i][0] > max:
        max = result[i][0]

for i in result:
    if result[i][0] == max:
        print(i, end=' ')
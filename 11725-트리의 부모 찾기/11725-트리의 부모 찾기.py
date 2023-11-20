import sys
from collections import deque

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = {}
for i in range(N):
    graph[i+1] = []
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = [0] * (N+1)

# BFS 문제풀이 1
def bfs(start_v):
    queue = deque()
    visited[start_v] = True
    queue.append(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                result[v] = cur_v

    return result

# DFS 문제풀이 2
def dfs(start_v):
    visited[start_v] = True
    for v in graph[start_v]:
        if not visited[v]:
            result[v] = start_v
            dfs(v)

bfs(1)
for i in range(2, len(result)):
    print(result[i])
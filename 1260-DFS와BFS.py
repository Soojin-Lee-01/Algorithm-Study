import sys
from collections import deque

def dfs(graph, cur_v, visited):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(graph, v, visited)

def bfs(graph, start_v):
    visited = []
    queue = deque([start_v])

    while queue:
        cur_v = queue.popleft()
        if cur_v not in visited:
            visited.append(cur_v)
            queue.extend(graph[cur_v])
    return visited

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    graph = {}
    for i in range(a):
        graph[i+1] = []
    for j in range(b):
        n, k = map(int, sys.stdin.readline().split())
        graph[n].append(k)
        graph[k].append(n)
    for key in graph:
        graph[key].sort()

    dfs_result = []
    dfs(graph, c, dfs_result)
    bfs_result = bfs(graph, c)

    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))

if __name__ == "__main__":
    main()
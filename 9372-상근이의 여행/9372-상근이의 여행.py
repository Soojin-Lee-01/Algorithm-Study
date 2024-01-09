import sys
from collections import deque

# Solution - 1
test = int(sys.stdin.readline())


def bfs(start_v):
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(start_v)
    visited[start_v] = True
    count = 0

    while queue:
        if count == n:
            return count
        cur_r = queue.popleft()
        for v in graph[cur_r]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                count += 1

    return count


for i in range(test):
    graph = {}
    n, m = map(int, sys.stdin.readline().split(' '))
    for k in range(n):
        graph[k+1] = []
    for j in range(m):
        a, b = map(int, sys.stdin.readline().split(' '))
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(1))

# Solution - 2
test_case = int(sys.stdin.readline())
graph_2= {}

for i in range(test_case):
    N, M = map(int, sys.stdin.readline().split(' '))
    for j in range(M):
        a, b = map(int, sys.stdin.readline().split(' '))
        graph_2[a] = b
        graph_2[b] = a
    print(N-1)
from collections import deque


def solution(n, computers):
    graph = {}
    for i in range(n):
        graph[i] = []

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    for i in range(len(graph)):
        graph[i] = set(graph[i])
    visited = [False for _ in range(n + 1)]

    def bfs(start_v):
        queue = deque()
        queue.append(start_v)
        visited[start_v] = True

        while queue:
            next_v = queue.popleft()
            for v in graph[next_v]:
                if visited[v] is False:
                    queue.append(v)
                    visited[v] = True

    count = 0
    for i in range(n):
        if visited[i] is False:
            bfs(i)
            count += 1

    return count


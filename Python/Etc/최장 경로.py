from collections import deque

test = int(input())

def dfs(x, cnt):
    global answer
    visited[x] = 1

    for k in graph[x]:
        if visited[k] == 0:
            visited[k]= 1
            dfs(k, cnt + 1)
    visited[x] = 0
    answer = max(answer, cnt)

for i in range(test):
    N, M = map(int, input().split())
    graph = {}
    for j in range(1, N+1):
        graph[j] = []
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    answer = 0
    for j in range(1, N+1):
        visited = [False for _ in range(N+1)]
        dfs(j, 1)
    print(f'#{i+1} {answer}')

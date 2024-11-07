def dfs(r, c):
    if r == 0:
        return c
 
    visited[r][c] = True
 
    if c > 0 and graph[r][c-1] == 1 and not visited[r][c-1]:
        return dfs(r, c-1)
 
    if c < 99 and graph[r][c+1] == 1 and not visited[r][c+1]:
        return dfs(r, c+1)
 
    return dfs(r-1, c)
 
 
for i in range(10):
    t = int(input())
 
    graph = []
    for j in range(100):
        data = list(map(int, input().split()))
        graph.append(data)
    visited = [[False] * 100 for _ in range(100)]
    for j in range(100):
        if graph[99][j] == 2:
            result = dfs(99, j)
            print(f'#{i+1} {result}')

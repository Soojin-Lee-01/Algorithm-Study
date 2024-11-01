R, C = map(int, input().split())

graph = []

for _ in range(R):
    data = list(input())
    graph.append(data)

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
answer = 0
alpha = set(graph[0][0])

def dfs(r, c, temp):
    global answer
    answer = max(answer, temp)

    for dr, dc in directions:
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < len(graph) and 0 <= next_c < len(graph[0]):
            if graph[next_r][next_c] not in alpha:
                alpha.add(graph[next_r][next_c])
                dfs(next_r, next_c, temp+1)
                alpha.remove(graph[next_r][next_c])

dfs(0, 0, 1)
print(answer)

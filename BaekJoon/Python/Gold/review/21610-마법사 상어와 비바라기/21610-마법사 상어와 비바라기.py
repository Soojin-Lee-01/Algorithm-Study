n, m = map(int, input().split())

graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
di = [(-1, 1), (1, -1), (1, 1), (-1, -1)]

for i in range(m):
    d, s = map(int, input().split())
    for j in range(len(cloud)):
        x, y = cloud[j]
        for _ in range(s):
            x = (x + directions[d - 1][0]) % n
            y = (y + directions[d - 1][1]) % n
        cloud[j] = (x, y)

    for x, y in cloud:
        graph[x][y] += 1
    temp_cloud = cloud.copy()
    cloud.clear()
    for cur_r, cur_c in temp_cloud:
        water = 0
        for dr, dc in di:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < n and 0 <= next_c < n:
                if graph[next_r][next_c] > 0:
                    water += 1
        graph[cur_r][cur_c] += water

    for a in range(len(graph)):
        for b in range(len(graph[0])):
            if (a, b) not in temp_cloud:
                if graph[a][b] >= 2:
                    cloud.append((a, b))
                    graph[a][b] -= 2
    temp_cloud.clear()
final = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        final += graph[i][j]

print(final)
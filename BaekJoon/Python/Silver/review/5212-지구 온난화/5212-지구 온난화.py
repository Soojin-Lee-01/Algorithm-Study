n, m = map(int, input().split(' '))

graph = []

for i in range(n):
    data = list(map(str, input().rstrip()))
    graph.append(data)


def bfs(r, c):
    count = 0
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < n and 0 <= next_c < m:
            if graph[next_r][next_c] == '.':
                count += 1
        else:
            count += 1

    if count >= 3:
        return True
    else:
        return False


result = []
sand = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'X':
            if bfs(i, j) == True:
                result.append((i, j))
            elif bfs(i, j) == False:
                sand.append((i, j))

for x, y in result:
    graph[x][y] = '.'

sand = sorted(sand, key=lambda x: (x[0], x[1]))
min_y = sand[0][0]
max_y = sand[len(sand) - 1][0]

sand = sorted(sand, key=lambda x: (x[1], x[0]))
min_x = sand[0][1]
max_x = sand[len(sand) - 1][1]

result_graph = []
for i in range(min_y, max_y + 1):
    t = []
    for j in range(min_x, max_x + 1):
        t.append(graph[i][j])
    result_graph.append(t)

for i in range(len(result_graph)):
    print(''.join(map(str, result_graph[i])))
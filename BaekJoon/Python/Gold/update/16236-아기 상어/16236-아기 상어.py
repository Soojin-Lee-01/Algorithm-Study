from collections import deque

N = int(input())
graph = []

for i in range(N):
    data = list(map(int, input().split(' ')))
    graph.append(data)

shark_x = 0
shark_y = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j


baby = 2
count = 0
eat = 0

def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0))
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    short_len = 0
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visi = []


    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        if (cur_r, cur_c) in fish:
            visi.append((cur_r, cur_c, cur_len))
        visi = sorted(visi, key=lambda x: (x[2], x[0], x[1]))
        for i in range(len(visi)):
            if visi[i][2] is not False:
                short_len = visi[i][0], visi[i][1], visi[i][2]
                break
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if 0 <= next_r < N and 0 <= next_c < N:
                if graph[next_r][next_c] <= baby or graph[next_r][next_c] == 9:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_len + 1))
                        visited[next_r][next_c] = True
    return short_len

while True:
    fish = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] < baby and graph[i][j] != 0:
                fish.append((i, j))

    if len(fish) == 0:
        print(count)
        exit()
    else:
        if bfs(shark_x, shark_y) == 0:
            print(count)
            exit()
        a, b, c = bfs(shark_x, shark_y)
        count += c
        eat += 1
        graph[a][b] = 9
        graph[shark_x][shark_y] = 0
        shark_x = a
        shark_y = b
    if eat == baby:
        baby += 1
        eat = 0








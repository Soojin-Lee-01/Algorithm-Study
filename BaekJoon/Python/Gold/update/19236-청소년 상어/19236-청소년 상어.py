# 구현 + dfs 문제!

import copy

graph = [[] for _ in range(4)]

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([data[2*j], data[2*j+1]-1])
    graph[i] = fish

max_score = 0

def dfs(sx, sy, score, graph):
    global max_score
    score += graph[sx][sy][0]
    max_score = max(max_score, score)
    graph[sx][sy][0] = 0

    # 물고기 움직
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if graph[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = graph[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + directions[nd][0]
            ny = f_y + directions[nd][1]
            if not (0 <= nx < 4 and  0<= ny < 4) or (nx == sx and ny == sy):
                continue
            graph[f_x][f_y][1] = nd
            graph[f_x][f_y], graph[nx][ny] = graph[nx][ny], graph[f_x][f_y]
            break

    # 상어 움직
    s_d = graph[sx][sy][1]
    for i in range(1, 5):
        nx = sx + directions[s_d][0] * i
        ny = sy + directions[s_d][1] * i
        if (0 <= nx < 4 and 0 <= ny < 4) and graph[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(graph))

dfs(0, 0, 0, graph)
print(max_score)
N, M, K = map(int, input().split())

graph = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def move(gra):
    temp_gra = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if gra[i][j]:
                for m, s, d in gra[i][j]:
                    ni = (i + directions[d][0] * s) % N
                    nj = (j + directions[d][1] * s) % N
                    temp_gra[ni][nj].append([m, s, d])
    return temp_gra

def dive(gra):
    temp_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(gra[i][j]) > 1:
                total_m = sum([x[0] for x in gra[i][j]])
                total_s = sum([x[1] for x in gra[i][j]])
                len_balls = len(gra[i][j])
                if total_m // 5 > 0:
                    new_m = total_m // 5
                    new_s = total_s // len_balls
                    is_all_even = all([x[2] % 2 == 0 for x in gra[i][j]])
                    is_all_odd = all([x[2] % 2 == 1 for x in gra[i][j]])
                    if is_all_even or is_all_odd:
                        new_directions = [0, 2, 4, 6]
                    else:
                        new_directions = [1, 3, 5, 7]
                    for d in new_directions:
                        temp_graph[i][j].append([new_m, new_s, d])
            elif len(gra[i][j]) == 1:
                temp_graph[i][j].extend(gra[i][j])
    return temp_graph

for _ in range(K):
    # 움직임
    graph = move(graph)
    # 2개 이상 있는 것 나눠짐
    graph = dive(graph)

# 결과 계산
result = 0
for i in range(N):
    for j in range(N):
        for m, s, d in graph[i][j]:
            result += m

print(result)

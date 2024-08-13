N, M, K = map(int, input().split())

# 추가할 양분
eat_graph = []

for _ in range(N):
    data = list(map(int, input().split()))
    eat_graph.append(data)

tree_graph = [[[] for _ in range(N)] for _ in range(N)]

# 나무 정보 담고, 나이가 적은 순부터 정렬
for _ in range(M):
    r, c, age = map(int, input().split())
    tree_graph[r-1][c-1].append(age)
    tree_graph[r-1][c-1].sort()

# 실제 양분 정보 그래프
graph = [[5 for _ in range(N)] for _ in range(N)]

# 봄
def spring(gra):
    # 죽은 나무의 정보
    die = []
    for i in range(len(gra)):
        for j in range(len(gra[0])):
            da = []
            if len(gra[i][j]) > 0:
                temp = gra[i][j]
                # 나무가 있으면 양분 먹고 나이 먹기
                for k in range(len(temp)):
                    if graph[i][j] >= temp[k]:
                        graph[i][j] -= temp[k]
                        da.append(temp[k]+1)
                    else:
                        # 양분이 부족하면 나무 죽음
                        die.append((temp[k], i, j))
                # 살아남은 나무 업데이트
                gra[i][j] = da

    return gra, die

# 여름
def summer(died):
    # 죽은 나무 양분되기
    for i in range(len(died)):
        plus, x, y = died[i]
        graph[x][y] += (plus//2)

# 가을
def autumn(gra):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(len(gra)):
        for j in range(len(gra[0])):
            if len(gra[i][j]) > 0:
                temp = gra[i][j]
                for k in range(len(temp)):
                    # 만약의 나무의 나이가 5의 배수면 상하좌우대각선 나무 생성
                    if temp[k] % 5 == 0:
                       for dr, dc in directions:
                            next_r = i + dr
                            next_c = j + dc
                            if 0 <= next_r < len(gra) and 0 <= next_c < len(gra[0]):
                                gra[next_r][next_c].append(1)
    return gra

# 나무 정렬
def sor():
    for i in range(len(tree_graph)):
        for j in range(len(tree_graph[0])):
            if len(tree_graph[i][j]) > 0:
                tree_graph[i][j].sort()

# 겨울 - 나무 양분 먹기
def winter():
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] += eat_graph[i][j]

for _ in range(K):
    tree_graph, die_tree = spring(tree_graph)
    summer(die_tree)
    tree_graph = autumn(tree_graph)
    sor()
    winter()

result = 0

# 총 나무 수 세기
for i in range(len(tree_graph)):
    for j in range(len(tree_graph[0])):
        if len(tree_graph[i][j]) > 0:
            result += len(tree_graph[i][j])
print(result)

# 도시의 크기와 정할 치킨집 갯수
n, m = map(int, input().split())

# 도시 그래프
graph = []

# 치킨 집 위치, 집의 위치
chicken = []
house = []

for i in range(n):
    data = list(map(int, input().split(' ')))
    graph.append(data)

for i in range(n):
    for j in range(n):

        # 치킨 집 위치 넣기
        if graph[i][j] == 2:
            chicken.append((i, j))

        # 집 위치 넣기
        elif graph[i][j] == 1:
            house.append((i, j))

# 조합 모두 담기
result = []


# 치킨집의 경우의 수 담기
def combi(n, start=0, combo=[]):
    if len(combo) == n:
        result.append(combo[:])
        return
    for i in range(start, len(chicken)):
        combo.append(chicken[i])
        combi(n, i + 1, combo)
        combo.pop()

    return result


min_value = int(1e9)


# 최소 거리 구하기 2
def find_dis(c):
    global min_value
    all_c = 0
    for h_x, h_y in house:
        min_c = 2 * n + 1
        for dr, dc in c:
            dist = (abs(h_x - dr) + abs(h_y - dc))
            min_c = min(min_c, dist)

        all_c += min_c

    min_value = min(min_value, all_c)


# 최소 거리 구하기 1
for c in combi(m):
    find_dis(c)

print(min_value)

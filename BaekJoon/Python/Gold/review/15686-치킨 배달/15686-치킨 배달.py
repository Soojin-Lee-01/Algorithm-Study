n, m = map(int, input().split())

graph = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

chicken = []
house = []

# 치킨의 좌표와 집의 좌표를 모두 담는다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        if graph[i][j] == 1:
            house.append((i, j))

# 치킨집의 조합
result = []
def combination(num, start = 0, combo =[]):
    if len(combo) == num:
        result.append(combo[:])
        return
    for i in range(start, len(chicken)):
        combo.append(chicken[i])
        combination(num, i+1, combo)
        combo.pop()

combination(m)

min_route = 1e9

# 치킨 집의 조합을 모두 비교해서 최소값을 찾는다.
for i in range(len(result)):
    temp = result[i]
    m = 0
    for j in range(len(house)):
        h_x, h_y = house[j]
        m_h = 1e9
        for k in temp:
            c_x, c_y = k
            route = abs(h_x-c_x) + abs(h_y-c_y)
            m_h = min(route, m_h)
        m += m_h
    min_route = min(m, min_route)

print(min_route)

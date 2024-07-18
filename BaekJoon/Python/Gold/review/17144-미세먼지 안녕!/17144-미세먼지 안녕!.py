# Solution - 1
import copy
from collections import deque
"""
deepcopy의 빈번한 사용은 시간초과를 일으킨다!
"""

R, C, T = map(int, input().split())
graph = []
graph_t = []
for i in range(R):
    data = list(map(int, input().split()))
    graph.append(data)


air = []
graph_t = graph[:]
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air.append((i, j))

temp_graph = [[0 for _ in range(C)] for _ in range(R)]
# 미세먼지 확산
def air_out(r, c, temp_graph):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    count = 0
    route = []
    for dr, dc in directions:
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < R and 0 <= next_c < C:
            if graph[next_r][next_c] != -1:
                count += 1
                route.append((next_r, next_c))


    for x, y in route:
        temp_graph[x][y] += graph[r][c] // 5
    temp_graph[r][c] += graph[r][c] - ((graph[r][c] // 5) * count)

for _ in range(T):
    # graph_t = copy.deepcopy(graph)
    temp_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                air_out(i, j, temp_graph)
                # graph = copy.deepcopy(graph_t)

    graph = temp_graph[:]
    for ax, ay in air:
        graph[ax][ay] = -1
    one = deque()
    one_t = []
    two = deque()
    two_t = []


    # 반시계
    for i in range(air[0][0]-1, -1, -1):
        one.append(graph[i][0])
        one_t.append((i, 0))
    for i in range(air[0][1]+1, C):
        one.append(graph[0][i])
        one_t.append((0, i))
    for i in range(air[0][1]+1, air[0][0]+1):
        one.append(graph[i][C-1])
        one_t.append((i, C-1))
    for i in range(C-2, 0, -1):
        one.append(graph[air[0][0]][i])
        one_t.append((air[0][0], i))



    # 시계

    for i in range(air[1][0]+1, R):
        two.append(graph[i][0])
        two_t.append((i, 0))
    for i in range(air[1][1]+1, C):
        two.append(graph[R-1][i])
        two_t.append((R-1, i))
    for i in range(R-2, air[1][0]-1, -1):
        two.append(graph[i][C-1])
        two_t.append((i, C-1))
    for i in range(C-2, air[1][1], -1):
        two.append(graph[air[1][0]][i])
        two_t.append((air[1][0], i))



    one.popleft()
    one.append(0)
    two.popleft()
    two.append(0)
    for xx, yy in one_t:
        graph[xx][yy] = one.popleft()
    for xx, yy in two_t:
        graph[xx][yy] = two.popleft()

result = 0
for k in range(R):
    result += sum(graph[k])

print(result+2)


# Solution - 2
import copy
from collections import deque
"""
deepcopy의 빈번한 사용은 시간초과를 일으킨다!
"""

R, C, T = map(int, input().split())
graph = []
graph_t = []
for i in range(R):
    data = list(map(int, input().split()))
    graph.append(data)
  
air = []
graph_t = graph[:]
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air.append((i, j))

temp_graph = [[0 for _ in range(C)] for _ in range(R)]

# 미세먼지 확산
def air_out(r, c, temp_graph):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    count = 0
    route = []
    for dr, dc in directions:
        next_r = r + dr
        next_c = c + dc
        if 0 <= next_r < R and 0 <= next_c < C:
            if graph[next_r][next_c] != -1:
                count += 1
                route.append((next_r, next_c))
              
    for x, y in route:
        temp_graph[x][y] += graph[r][c] // 5
    temp_graph[r][c] += graph[r][c] - ((graph[r][c] // 5) * count)

for _ in range(T):
    temp_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                air_out(i, j, temp_graph)

    graph = temp_graph[:]
    for ax, ay in air:
        graph[ax][ay] = -1
    one = deque()
    one_t = []
    two = deque()
    two_t = []

    # 반시계
    for i in range(air[0][0]-1, -1, -1):
        one.append(graph[i][0])
        one_t.append((i, 0))
    for i in range(air[0][1]+1, C):
        one.append(graph[0][i])
        one_t.append((0, i))
    for i in range(air[0][1]+1, air[0][0]+1):
        one.append(graph[i][C-1])
        one_t.append((i, C-1))
    for i in range(C-2, 0, -1):
        one.append(graph[air[0][0]][i])
        one_t.append((air[0][0], i))

    # 시계
    for i in range(air[1][0]+1, R):
        two.append(graph[i][0])
        two_t.append((i, 0))
    for i in range(air[1][1]+1, C):
        two.append(graph[R-1][i])
        two_t.append((R-1, i))
    for i in range(R-2, air[1][0]-1, -1):
        two.append(graph[i][C-1])
        two_t.append((i, C-1))
    for i in range(C-2, air[1][1], -1):
        two.append(graph[air[1][0]][i])
        two_t.append((air[1][0], i))

    one.popleft()
    one.append(0)
    two.popleft()
    two.append(0)
    for xx, yy in one_t:
        graph[xx][yy] = one.popleft()
    for xx, yy in two_t:
        graph[xx][yy] = two.popleft()

result = 0
for k in range(R):
    result += sum(graph[k])

print(result+2)



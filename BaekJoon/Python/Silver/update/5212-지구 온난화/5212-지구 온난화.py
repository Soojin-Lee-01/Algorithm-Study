import sys

r, c = map(int ,sys.stdin.readline().split(' '))
graph = []
for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

result = [] # 잠기게 되는 좌표

for i in range(r):
    for j in range(c):
        if graph[i][j] == "X":
            count = 0
            for dx, dy in directions:
                next_r = i + dx
                next_c = j + dy
                if next_r >= 0 and next_r < r and next_c >= 0 and next_c < c:
                    if graph[next_r][next_c] == ".":
                        count += 1
                else:
                    count += 1
                    continue
            if count >= 3:
                result.append((i, j))

if len(result) > 0:
    for x, y in result:
        graph[x][y] = '.'

x1, y1, x2, y2 = 0, c-1, 0, 0

for i in range(0, r):
    if 'X' in graph[i]:
        x1 = i
        break
for i in range(r-1, -1, -1):
    if 'X' in graph[i]:
        x2 = i
        break

for i in range(x1, x2+1):
    for j in range(c):
        if graph[i][j] == "X":
            y1 = min(y1, j)
            y2 = max(y2, j)

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        print(graph[i][j], end='')
    print()
n, m = map(int, input().split(' '))

graph = []

for i in range(n):
    data = list(map(int, input().split(' ')))
    graph.append(data)


cur_d = {(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)}

def simu(r, c, cur_d=None):
    global cur_r, cur_c
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    # 1. 이동
    for _ in range(c):
        new_cur_d = set()
        for dr, dc in cur_d:
            cur_r, cur_c = dr, dc
            cur_r = cur_r + directions[r - 1][0]
            cur_c = cur_c + directions[r - 1][1]
            if cur_r == n:
                cur_r = 0
            if cur_c == n:
                cur_c = 0
            if cur_r == -1:
                cur_r = n - 1
            if cur_c == -1:
                cur_c = n - 1
            new_cur_d.add((cur_r, cur_c))
        cur_d = new_cur_d

    # 2. 이동 후 비 내림
    for dr, dc in cur_d:
        graph[dr][dc] += 1

    # 3. 대각선 확인후 물 추가
    for dr, dc in cur_d:
        for i in range(1, 9, 2):
            if dr+directions[i][0] >= 0 and dr+directions[i][0] < n and dc + directions[i][1] >= 0 and dc + directions[i][1] < n:
                if graph[dr+directions[i][0]][dc + directions[i][1]] > 0:
                    graph[dr][dc] += 1

    temp_cur = set(cur_d)
    cur_d.clear()
    # 4. 마지막 구름 생긴 후 물의 양 적어짐
    for i in range(n):
        for j in range(n):
            if (i, j) not in temp_cur:
                if graph[i][j] >= 2:
                    cur_d.add((i, j))
                    graph[i][j] -= 2

    return cur_d


for i in range(m):
    a, b = map(int, input().split(' '))
    cur_d = simu(a, b, cur_d=cur_d)

count = 0
for i in range(n):
    for j in range(n):
        count += graph[i][j]

print(count)



N, M = map(int, input().split())

graph = []
for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

# CCTV 정보 담기
temp = []
# 원래 안전구역 갯수 담기
count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count += 1
        elif graph[i][j] != 6:
            temp.append([graph[i][j], i, j])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

direct = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def move(r, c, dire, temp_graph):
    for d in dire:
        nx, ny = r, c
        while True:
            nx += directions[d][0]
            ny += directions[d][1]

            if not (0 <= nx < N and 0 <= ny < M) or temp_graph[nx][ny] == 6:
                break
            if temp_graph[nx][ny] != 0:
                continue
            temp_graph[nx][ny] = '#'


def zero(temp_graph):
    cnt = 0
    for row in temp_graph:
        cnt += row.count(0)
    return cnt


def dfs(level, temp_graph):
    global count

    if level == len(temp):
        count = min(count, zero(temp_graph))
        return

    number, x, y = temp[level]

    original_graph = [row[:] for row in temp_graph]  # 원본 상태 저장

    for d in direct[number]:
        move(x, y, d, temp_graph)
        dfs(level + 1, temp_graph)
        temp_graph = [row[:] for row in original_graph]  # 상태 복구


# 초기 상태에서 DFS 시작
count = zero(graph)  # 초기 상태의 안전구역 갯수
dfs(0, graph)  

print(count)

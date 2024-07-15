
# 첫번째 풀이 - 빡구현, 완전 탐색
n, m = map(int, input().split())
graph = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

te = [
[(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]


max_num = 0

for i in range(n):
    for j in range(m):
        for s in te:
            total = 0
            for k in range(4):
                next_r = i + s[k][0]
                next_c = j + s[k][1]
                if 0 <= next_r < n and 0 <= next_c < m:
                    total += graph[next_r][next_c]
                if total > max_num:
                    max_num = total
print(max_num)


# 두번째 풀이는 dfs로 테트로미노를 구현하는 것
n, m = map(int, input().split())

graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

max_num = 0
visited = [[False for _ in range(m)] for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, count,total):
    global max_num
    if count == 4:
        max_num = max(total, max_num)
        return
    for i in range(4):
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count+1, total+graph[nx][ny])
            visited[nx][ny] = False


def solution(a, b):
    global max_num
    tetromino_shapes = [
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(1, 0), (1, 1), (0, 1), (2, 1)],
        [(1, 0), (1, 1), (1, 2), (0, 1)]
    ]

    for shape in tetromino_shapes:
        total = 0
        for dx, dy in shape:
            nx = a + dx
            ny = b + dy
            if 0 <= nx < n and 0 <= ny < m:
                total += graph[nx][ny]
            else:
                break
        max_num = max(max_num, total)


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
        solution(i, j)

print(max_num)

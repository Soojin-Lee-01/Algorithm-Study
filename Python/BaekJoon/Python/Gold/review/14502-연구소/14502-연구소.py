from collections import deque
import copy

n, m = map(int, input().split())

graph = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

vir = []

# 그래프를 깊은 복사해준다.
temp_graph = copy.deepcopy(graph)

target = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            vir.append((i, j))
        if graph[i][j] == 2:
            target.append((i, j))

result = []
# 조합
def combination(n, start = 0, combo = []):
    if len(combo) == 3:
        result.append(combo[:])
        return
    for i in range(start, len(vir)):
        combo.append(vir[i])
        combination(n, i+1, combo)
        combo.pop()


combination(3)

def bfs(nums):
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    for a, b in nums:
        queue.append((a, b))
        visited[a][b] = True
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < n and 0 <= next_c < m:
                if not visited[next_r][next_c]:
                    if graph[next_r][next_c] == 0:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        graph[next_r][next_c] = 2

    return graph

max_n = 0


def cou(gra):
    count = 0
    for q in range(n):
        for w in range(m):
            if gra[q][w] == 0:
                count += 1
    return count

for i in range(len(result)):
    temp = result[i]
    for x, y in temp:
        graph[x][y] = 1
    bfs(target)
    co = cou(graph)
    max_n = max(max_n, co)
    # 깊은 복사 해준다.
    graph = copy.deepcopy(temp_graph)
print(max_n)

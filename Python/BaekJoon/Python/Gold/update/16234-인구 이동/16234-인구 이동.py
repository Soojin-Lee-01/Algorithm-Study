from collections import deque

N, L, R = map(int, input().split())

# 인구 그래프
graph = []

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

# 국경을 개방하고, 평균으로 바꿔준다
def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    da = [(r, c)]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c]:
                    if L <= abs(graph[next_r][next_c] - graph[cur_r][cur_c]) <= R:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        da.append((next_r, next_c))
    # 만약에 국경을 개방할 수 있는 나라가 없다면
    if len(da) < 2:
        return 0
    # 국경을 개방할 수 있는 나라가 있다면
    else:
        result = 0
        for x, y in da:
            result += graph[x][y]
        result = result // len(da)
        # 평균으로 바꿔준다.
        for x, y in da:
            graph[x][y] = result
        return 1

# 날을 추가한다.
day = 0


while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for k in range(N):
        for j in range(N):
            if not visited[k][j]:
                count += bfs(k, j)
    # 만약에 국경을 개방하는 나라가 없다면 정지
    if count == 0:
        break
    else:
        day += 1

print(day)

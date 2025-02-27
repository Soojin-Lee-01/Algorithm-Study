from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 가장 큰 블럭 찾기
def big_block(r, c):
    temp_block = []
    color_block = []
    same = graph[r][c]
    queue = deque()
    temp_block.append((r, c))
    queue.append((r, c))

    visited[r][c] = True
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    while queue:
        cur_r, cur_c = queue.popleft()

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                if graph[next_r][next_c] == 0:
                    queue.append((next_r, next_c))
                    color_block.append((next_r, next_c))
                    visited[next_r][next_c] = True
                elif graph[next_r][next_c] == same:
                    queue.append((next_r, next_c))
                    temp_block.append((next_r, next_c))
                    visited[next_r][next_c] = True

    for x, y in color_block:
        visited[x][y] = False

    return [len(temp_block) + len(color_block), len(color_block), temp_block + color_block]

# 점수 더하고, 가장 큰 블럭 빈 값으로 처리
def score_and_blank(block_data):
    global answer
    answer += len(block_data) ** 2
    for r, c in block_data:
        graph[r][c] = -2

# 90도 반시계 회전
def reverse_90(gra):
    return list(map(list, zip(*gra)))[::-1]

# 중력 작용 : 아래에서 위로 탐색한다!
def gravity():
    for c in range(N):
        for r in range(N-2, -1, -1):
            if graph[r][c] >= 0:
                nr = r
                while nr + 1 < N and graph[nr+1][c] == -2:
                    nr += 1
                if nr != r:
                    graph[nr][c], graph[r][c] = graph[r][c], -2

# 메인 로직
answer = 0 # 점수
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]

    target_block = []

    # 가장 큰 블럭 찾기
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and not visited[i][j]:
                block_info = big_block(i, j)

                if block_info[0] >= 2:
                    target_block.append(block_info)

    # 만약 블록 그룹이 없다면 종료
    if not target_block:
        break

    # 정렬 : 크기 -> 무지개 블럭 개수 -> 기준 블럭 행 -> 기준 블럭 열
    target_block.sort(reverse=True, key=lambda x : (x[0], x[1], x[2][0][0], x[2][0][1]))

    # 점수 반영 및 가장 큰 블럭 제거
    score_and_blank(target_block[0][2])

    # 중력 작용
    gravity()

    # 반시계 회전
    graph = reverse_90(graph)

    # 중력 작용
    gravity()

print(answer)

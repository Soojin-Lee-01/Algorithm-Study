from collections import deque

def solution(land):
    # 방문 여부를 체크하기 위한 2차원 리스트
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    # 각 영역의 크기와 영역 번호를 저장할 2차원 리스트
    data = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]

    # BFS를 이용하여 영역 탐색
    def bfs(r, c, k):
        queue = deque([(r, c)])
        visited[r][c] = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        temp = [(r, c)]
        count = 1

        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in directions:
                next_r, next_c = cur_r + dr, cur_c + dc
                if 0 <= next_r < len(land) and 0 <= next_c < len(land[0]):
                    if not visited[next_r][next_c] and land[next_r][next_c] == 1:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        temp.append((next_r, next_c))
                        count += 1

        # 탐색한 영역의 크기와 영역 번호를 data에 기록
        for x, y in temp:
            data[x][y] = (count, k)

    k = 0  # 영역 번호

    # 전체 땅을 순회하며 BFS로 각 영역 탐색
    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j, k)
                k += 1

    answer = []

    # 각 열에서 포함된 모든 영역의 크기 합산
    for i in range(len(land[0])):
        total_area = 0
        unique_areas = set()
        for j in range(len(land)):
            if data[j][i] != 0 and data[j][i][1] not in unique_areas:
                total_area += data[j][i][0]
                unique_areas.add(data[j][i][1])
        answer.append(total_area)

    return max(answer)

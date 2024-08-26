n = int(input())
data = [list(map(int, input().split())) for _ in range(n**2)]

# 이미 채워진 확정 그래프
graph = [[0 for _ in range(n)] for _ in range(n)]

# 인접 좋아하는 사람, 인접 0 count 넣기
temp = []

# 인접한 기준, 상하좌우
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(len(data)):
    # 만약에 처음이라면 1, 1에 넣음
    if i == 0:
        graph[1][1] = data[i][0]
    else:
        for j in range(n):
            for k in range(n):
                if graph[j][k] == 0:
                    empty_count = 0
                    like_count = 0
                    for dr, dc in directions:
                        next_r = j + dr
                        next_c = k + dc
                        if 0 <= next_r < n and 0 <= next_c < n:
                            # 인접한 좋아하는 사람 수
                            if graph[next_r][next_c] in data[i][1:]:
                                like_count += 1
                            # 인접한 0의 수
                            elif graph[next_r][next_c] == 0:
                                empty_count += 1
                        temp.append((j, k, like_count, empty_count))
        # 좋아하는 사람 수 -> 인접한 0 사람 수 -> 행 -> 열
        temp = sorted(temp, key=lambda x: (-x[2], -x[3], x[0], x[1]))
        graph[temp[0][0]][temp[0][1]] = data[i][0]
    temp = []

final = 0
# 딕셔너리로 좋아하는 사람 관리
dic = {person[0]: person[1:] for person in data}

for i in range(n):
    for j in range(n):
        count_likes = 0
        for dr, dc in directions:
            next_r = i + dr
            next_c = j + dc
            if 0 <= next_r < n and 0 <= next_c < n:
                if graph[next_r][next_c] in dic[graph[i][j]]:
                    count_likes += 1
        if count_likes == 1:
            final += 1
        elif count_likes == 2:
            final += 10
        elif count_likes == 3:
            final += 100
        elif count_likes == 4:
            final += 1000

print(final)

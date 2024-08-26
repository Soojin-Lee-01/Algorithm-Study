n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

# 북, 동, 남, 서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 청소한 영역
count = 0

# 청소할 수 있다면 청소하고 청소한 영역 +1
def clean(cur_r, cur_c):
    global count
    if graph[cur_r][cur_c] == 0:
        graph[cur_r][cur_c] = 2
        count += 1
        return True
    return False
# 동서남북 청소할 수 있는 영역 존재 여부 확인
def rotate(cur_r, cur_c):
    for dr, dc in directions:
        next_r = cur_r + dr
        next_c = cur_c + dc
        if (0 <= next_r < n and 0 <= next_c < m):
            if graph[next_r][next_c] == 0:
                return True
    return False
# 반시계 방향으로 돌면서 가능한 방향 찾는다.
def rot(cur_r, cur_c, di):
    for i in range(4):
        di = (di + 3) % 4
        temp_r = cur_r + directions[di][0]
        temp_c = cur_c + directions[di][1]
        if 0 <= temp_r < n and 0 <= temp_c < m:
            if graph[temp_r][temp_c] == 0:
                return temp_r, temp_c, di
    return False

while True:
    # 현재 칸 청소되지 않은 경우, 칸 청소
    clean(r, c)
    # 동서남북 청소할 수 있는 영역 있다면, 반시계 방향 회전 후, 전진
    if rotate(r, c) is True:
        da = rot(r,c,d)
        if da:
            r = da[0]
            c = da[1]
            d = da[2]
    # 청소할 수 있는 영역이 없다면
    else:
        back_d = (d + 2) % 4
        r += directions[back_d][0]
        c += directions[back_d][1]
        if not (0 <= r < n and 0 <= c < m) or graph[r][c] == 1:
            break
print(count)
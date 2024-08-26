n, m , x, y, k = map(int, input().split())

graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

data = list(map(int, input().split()))

# 각 주사위의 숫자 표시위해
dice = [0 for _ in range(6)]

# 동서남북 이동에 따른 주사위 순서 변화
def turn(num):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽일 경우
    if num == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, f, c, e, b, d
    # 서쪽일 경우
    elif num == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = a, e, c, f, d, b
    # 북쪽일 경우
    elif num == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, a, b, c, e, f
    # 남쪽일 경우
    elif num == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, c, d, a, e, f

    return dice
r = x
c = y
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for i in range(len(data)):
    d = data[i]
    next_r = r + directions[d-1][0]
    next_c = c + directions[d-1][1]
    # 지도에서 벗어나는지 확인
    if 0 <= next_r < n and 0 <= next_c < m:
        r = next_r
        c = next_c
        # 주사위 굴리기
        turn(d)
        # 만약에 지도위에 0이 아니면, 주사위에 칸에 적혀있는 숫자가 복사
        if graph[r][c] != 0:
            dice[1] = graph[r][c]
            graph[r][c] = 0
        # 만약에 지도위가 0이면, 주사위에 적혀있는 숫자가 칸에 복사
        elif graph[r][c] == 0:
            graph[r][c] = dice[1]
        print(dice[3])

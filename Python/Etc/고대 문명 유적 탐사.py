from collections import deque

K, M = map(int, input().split())

graph = []

for i in range(5):
    data = list(map(int, input().split()))
    graph.append(data)

fill = list(map(int, input().split()))

def return_graph():

    temp_graph = []
    for i in range(5):
        datt = []
        for j in range(5):
            datt.append(graph[i][j])
        temp_graph.append(datt)

    return temp_graph

def rect(r, c):
    temp_graph = []
    for i in range(r, r+3):
        t = []
        for j in range(c, c+3):
            t.append(graph[i][j])
        temp_graph.append(t)

    return temp_graph

def bfs(t_graph):

    def bbfs(r, c):

        queue = deque()
        queue.append((r, c))
        visited[r][c] = True
        cc = 1
        ro = [(r, c)]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if 0 <= next_r < 5 and 0 <= next_c < 5:
                    if not visited[next_r][next_c]:
                        if t_graph[next_r][next_c] == t_graph[cur_r][cur_c]:
                            cc += 1
                            ro.append((next_r, next_c))
                            queue.append((next_r, next_c))
                            visited[next_r][next_c] = True
        if cc >= 3:
            return cc, ro
        else:
            return 0
    count = 0
    route = []
    visited = [[False for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                a = bbfs(i, j)
                if a != 0:
                    count += a[0]
                    route += a[1]

    return count, route

def rotate_90(temp):
    # 이제 각도 돌리기
    temp = zip(*(temp[::-1]))

    temp = [list(a) for a in temp]

    return temp


def rotate_180(temp):
    temp = rotate_90(rotate_90(temp))

    return temp

def rotate_270(temp):
    temp = rotate_90(rotate_90(rotate_90(temp)))

    return temp

def new_graph(r, c, temp, gra, ro):
    global answer, rota, x, y
    global fill_data

    for i in range(r, r+3):
        for j in range(c, c+3):
            temp[i][j] = gra[i-r][j-c]

    da = bfs(temp)

    if answer < da[0]:
        answer = da[0]
        fill_data = da[1]
        rota = ro
        x = r
        y = c

    elif answer == da[0]:
        if ro < rota:
            rota = ro
            answer = da[0]
            fill_data = da[1]
            x = r
            y = c
        elif ro == rota:
            if y > c:
                answer = da[0]
                fill_data = da[1]
                x = r
                y = c
                rota = ro
            elif x > r:
                answer = da[0]
                fill_data = da[1]
                x = r
                y = c
                rota = ro


def fill_new(x, y, rota, fill_data):
    global graph, first_index, answer

    te = rect(x, y)
    final = [[0 for _ in range(3)] for _ in range(3)]
    if rota == 0:
        final = rotate_90(te)
    elif rota == 1:
        final = rotate_180(te)
    elif rota == 2:
        final = rotate_270(te)

    # 최종 바꾸기
    for i in range(x, x + 3):
        for j in range(y, y+3):

            graph[i][j] = final[i-x][j-y]

    while (True):
        fill_data = sorted(fill_data, key=lambda x : (x[1], -x[0]))


        for a, b in fill_data:
            graph[a][b] = fill[first_index]
            first_index += 1
            if first_index == M:
                first_index = 0


        fina = bfs(graph)

        if fina[0] == 0:
            break
        else:
            answer += fina[0]
            fill_data = fina[1]

first_index = 0
for _ in range(K):
    fill_data = []
    answer = -1
    x = 100000
    y = 1000000
    rota = 10000
    temp_graph = return_graph()


    for i in range(0, 3):
        for j in range(0, 3):
            rotate_da = []
            # 작은 그래프 추출

            temp = rect(i, j)
            #print(temp)
            # 추출한 그래프 회전 각도 - 90 (반환값, bfs 값과, 갯수)
            new = rotate_90(temp)
            #print("90", new)
            new_graph(i, j, temp_graph, new, 0)
            temp_graph = return_graph()
            # 추출한 그래프 회전 각도 - 180
            new = rotate_180(temp)
            #print("180", new)
            new_graph(i, j, temp_graph, new, 1)
            temp_graph = return_graph()
            # 추출한 그래프 회전 각도 - 270
            new = rotate_270(temp)
            #print("270", new)
            new_graph(i, j, temp_graph, new, 2)
            temp_graph = return_graph()


    if answer == 0:
        break
    # 새로운거 채워넣기
    fill_new(x, y, rota, fill_data)

    print(answer, end=' ')

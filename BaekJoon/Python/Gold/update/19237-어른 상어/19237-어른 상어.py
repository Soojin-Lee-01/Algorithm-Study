N, M, K = map(int, input().split(' '))

data = []
for _ in range(N):
    data.append(list(map(int, input().split(' '))))

shark = [[0, 0] for _ in range(M)]

directions = list(map(int, input().split(' ')))

prior = []
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split(' '))))
    prior.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

smell = [[[0, 0]] * N for _ in range(N)]

def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], K]


def move():
    new_data = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if data[x][y] != 0:
                direction = directions[data[x][y]-1]
                found = False
                for idx in prior[data[x][y]-1][direction-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][1] == 0:
                            directions[data[x][y]-1] = idx
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else:
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True
                            break
                if found:
                    continue

                for idx in prior[data[x][y] -1][direction-1]:
                    nx = x + dx[idx-1]
                    ny = y + dy[idx-1]
                    if 0 <= nx < N and 0 <= ny < N:
                        if smell[nx][ny][0] == data[x][y]:
                            directions[data[x][y]-1] = idx
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data


answer = 0
while True:
    update_smell()
    new_data = move()
    data = new_data
    answer += 1

    check = True
    for i in range(N):
        for j in range(N):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break
    if answer >= 1000:
        print(-1)
        break

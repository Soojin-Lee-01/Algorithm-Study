N, M = map(int, input().split())
graph = []
for _ in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
cloud = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move(d, s): # 비구름이 있는 곳
    global cloud
    new_cloud = set()
    for dr, dc in cloud:
        for _ in range(s):
            dr = dr + dx[d-1]
            dc = dc + dy[d-1]
            if dr == -1:
                dr = N -1
            if dr == N:
                dr = 0
            if dc == -1:
                dc = N-1
            if dc == N:
                dc = 0
        new_cloud.add((dr, dc))
        cloud = new_cloud

def upgrade():
    global cloud
    for dr, dc in cloud:
        graph[dr][dc] += 1
    for dr, dc in cloud:
        temp = 0
        for i in range(1, 8, 2):
            next_r = dr + dx[i]
            next_c = dc + dy[i]
            if 0 <= next_r < N and 0 <= next_c < N:
                if graph[next_r][next_c] > 0:
                    temp += 1
        graph[dr][dc] += temp

def find():
    global cloud
    temp = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in cloud:
                if graph[i][j] >= 2:
                    temp.add((i, j))
    cloud = temp
    for dr, dc in cloud:
        graph[dr][dc] -= 2

for i in range(M):
    d, s = map(int, input().split())
    move(d, s)

    upgrade()
    find()

result = 0
for i in range(N):
    for j in range(N):
        result += graph[i][j]
print(result)

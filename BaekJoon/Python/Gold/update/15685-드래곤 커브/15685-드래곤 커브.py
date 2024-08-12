"""
규칙을 찾자!
-> / 위
위 / <-
<- / 아래
아래 / ->

"""
num = int(input())

graph = [[0 for _ in range(101)] for _ in range(101)]

# 규칙 순!
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for _ in range(num):
    x, y, d, g = map(int, input().split(' '))
    graph[x][y] = 1

    move = [d]

    # 규칙에 의해서 순서를 담자!
    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i-1]+1) % 4)
        move.extend(temp)

    # 규칙대로 움직여주자!
    for i in move:
        next_r = x + directions[i][0]
        next_c = y + directions[i][1]
        graph[next_r][next_c] = 1
        x, y = next_r, next_c

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            answer += 1

print(answer)

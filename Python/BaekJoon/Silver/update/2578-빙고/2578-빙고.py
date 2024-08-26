import sys

graph = [] # 빙고판
for i in range(5):
    data = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(data)

speak = [] # 사회자가 부르는 순서
for i in range(5):
    num = map(int, sys.stdin.readline().rstrip().split(' '))
    speak.extend(num)

def find_location(s, bingboard): # 좌표 위치 찾기
    for i, key in enumerate(bingboard):
        if s in key:
            return i, key.index(s)
    return None

bingo = []

def col(gra, x): # 열에서 빙고 찾기
    count = 0
    for i in range(5):
        if gra[x][i] == -1:
            count += 1
        if count == 5:
            return True
    return False

def row(gra, x): # 행에서 빙고 찾기
    count = 0
    for i in range(5):
        if gra[i][x] == -1:
            count += 1
        if count == 5:
            return True
    return False

def diga1(gra): # 왼쪽 대각선
    if (gra[0][0] == -1 and gra[1][1] == -1 and gra[2][2] == -1 and gra[3][3] == -1 and gra[4][4] == -1):
        return True
    return False

def diga2(gra): # 오른쪽 대각선
    if (gra[0][4] == -1 and gra[1][3] == -1 and gra[2][2] == -1 and gra[3][1] == -1 and gra[4][0] == -1):
        return True
    return False

for i in speak:
    bingo.append(find_location(i, graph))

result = 0
for x, y in bingo:
    graph[x][y] = -1
    for j in range(5):
        if col(graph, j) is True:
            result += 1
        if row(graph, j) is True:
            result += 1
    if diga1(graph) is True:
        result += 1
    if diga2(graph) is True:
        result += 1
    if result >= 3:
        print(bingo.index((x, y)) + 1)
        break
    result = 0






import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split(' '))

graph = []
for i in range(R):
    data = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(data)

def bfs(r, c):
    queue = deque()
    queue.append((r,c))
    direction = [(-1,0),(0,-1),(1,0),(0,1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        for dx, dy in direction:
            next_r = cur_r + dx
            next_c = cur_c + dy
            if next_r >= 0 and next_r < len(graph) and next_c >= 0 and next_c < len(graph[0]):
                if graph[next_r][next_c] == "S":
                    return False

    return True

result = -1
for i in range(R):
    for j in range(C):
        if graph[i][j] == "W":
            if bfs(i, j) is False:
                result = 0
                break
            else:
                result = 1
                break

if result == 0: # 울타리를 설치 할 수 없음
    print(0)
else:
    print(1) # 울타리 설치할 수 있음. 모든 . 에 울타리 설치
    for i in range(R):
        for j in range(C):
            if graph[i][j] == ".":
                graph[i][j] = "D"
            print(graph[i][j], end='')
        print()






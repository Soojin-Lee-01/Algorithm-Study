from collections import deque

n, m = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)] # 그래프 구성
temp = [[0] * m for _ in range(n)] # temp 그래프 구성

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 상하좌우 이동

queue = deque()
result = 0
def bfs(): # 바이러스가 퍼짐
    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if 0 <= next_r < n and 0 <= next_c < m:
                if temp[next_r][next_c] == 0:
                    queue.append((next_r, next_c))
                    temp[next_r][next_c] = 2 # 바이러스 퍼짐

def wall(cnt):
    if cnt == 3: # 만약에 벽이 3개 다 세워진다면
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
                if temp[i][j] == 2: # 만약에 바이러스가 있는 위치라면 큐에 담아준다.
                    queue.append((i, j))

        bfs() # 바이러스를 퍼트린다.
        area = 0
        global result

        for i in range(n):
            area += temp[i].count(0) # 안전 영역 크기를 구한다.

        result = max(result, area) # 안전 영역의 크기가 큰걸 결과에 대입
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 만약에 빈칸이면
                graph[i][j] = 1 # 벽을 세운다.
                wall(cnt+1) # 벽을 하나 더해준다. -> 재귀
                graph[i][j] = 0 # 벽을 없앤다.

wall(0) # 처음은 벽이 없다.
print(result)
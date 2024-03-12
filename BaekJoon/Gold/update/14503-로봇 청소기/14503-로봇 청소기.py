"""
북동남서의 위치를 제대로 파악하자!
반시계 방향으로 90도 -> (d + 3) % 4
180도로 방향 전환 -> (d + 2) % 4
분석한 시간복잡도 : O(n*m)
"""

import sys

n, m = map(int, sys.stdin.readline().split(' '))

r, c, d = map(int, sys.stdin.readline().split(' '))

graph = []

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(data)

count = 0 # 청소한 칸의 갯수

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서

while True:
    okay = 0 # 회전 유무 판단
    clean = 0 # 청소할 수 있는 칸의 갯수 (동서남북 중)

    if graph[r][c] == 0:
        count += 1
        graph[r][c] = 2  # 청소 완료

    for dr, dc in directions: # 동서남북 중 청소할 수 있는 칸의 갯수 파악
        next_r = dr + r
        next_c = dc + c
        if 0 <= next_r < n and 0 <= next_c < m:
            if graph[next_r][next_c] == 0:
                clean += 1

    if clean == 0: # 청소할 수 있는 칸의 갯수가 없다면
        back_d = (d + 2) % 4  # 현재 방향에서 180도 회전한 방향
        next_r = r + directions[back_d][0]
        next_c = c + directions[back_d][1]
        if 0 <= next_r < n and 0 <= next_c < m and graph[next_r][next_c] != 1: # 후진이 가능하다면 후진
            r = next_r
            c = next_c
        else: # 아니면 종료
            break
    else: # 청소할 수 있는 칸의 갯수가 있다면
        while okay == 0:
            d = (d + 3) % 4  # 반시계 방향으로 90도 회전
            next_r = r + directions[d][0]
            next_c = c + directions[d][1]
            if 0 <= next_r < n and 0 <= next_c < m and graph[next_r][next_c] == 0: # 청소할 수 있다면 이동
                r = next_r
                c = next_c
                okay = 1

print(count)

"""
BFS로 풀이
시간복잡도 : 최대 O(N * N * N)
"""
from collections import deque

N = int(input())

graph = []

min_num = 1000
max_num = 0

for _ in range(N):
    data = list(map(int, input().split()))
    max_num = max(max(data), max_num)
    min_num = min(min(data), min_num)
    graph.append(data)


def bfs(r, c, target):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c] and graph[next_r][next_c] > target:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True

answer = 1
for k in range(min_num, max_num+1):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > k:
                bfs(i, j, k)
                count += 1


    answer = max(answer, count)

print(answer)

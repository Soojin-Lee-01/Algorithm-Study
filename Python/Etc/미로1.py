"""
시간복잡도를 분석해보자.
O(n*n*10)
"""

from collections import deque

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited = [[False for _ in range(16)] for _ in range(16)]
    visited[r][c] = True

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        cur_r, cur_c = queue.popleft()
        if graph[cur_r][cur_c] == 3:
            return 1
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < 16 and 0 <= next_c < 16:
                if graph[next_r][next_c] == 0 or graph[next_r][next_c] == 3:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
    return 0

for _ in range(10):
    n = int(input())
    graph = []
    answer = -1
    for _ in range(16):
        data = list(map(int, input()))
        graph.append(data)
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                answer = bfs(i, j)
                break
    print(f'#{n} {answer}')

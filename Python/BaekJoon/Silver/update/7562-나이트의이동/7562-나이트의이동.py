from collections import deque

def bfs(r, c):
    global n, x, y
    queue = deque()
    queue.append((r, c, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]

    visited[r][c] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()

        if cur_r == x and cur_c == y:
            return cur_len

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if 0 <= next_r < n and 0 <= next_c < n:
                if not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True
    return -1

directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

test = int(input())

for _ in range(test):
    n = int(input())
    start_x, start_y = map(int, input().split())
    x, y = map(int, input().split())
    print(bfs(start_x, start_y))

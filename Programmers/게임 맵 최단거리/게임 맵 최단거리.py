from collections import deque


def solution(maps):
    answer = 0
    queue = deque()
    queue.append((0, 0, 0))
    visited = [[False for _ in range(len(maps))] for _ in range(len(maps))]
    visited[0][0] = True
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()

        if cur_r == len(maps) - 1 and cur_c == len(maps) - 1:
            return cur_len
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < len(maps) and 0 <= next_c < len(maps):
                if maps[next_r][next_c] == 1:
                    if not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_len + 1))
                        visited[next_r][next_c] = True
    return -1




"""
BFS를 이용해 풀자
"""
from collections import deque

N, K = map(int, input().split())

def bfs(n, target):
    queue = deque()
    queue.append((n, 0))
    visited = [False for _ in range(100001)]

    while queue:
        cur_r, cur_len = queue.popleft()
        if cur_r == target:
            return cur_len
        for next_r in (cur_r + 1, cur_r -1, cur_r *2):
            if 0 <= next_r < 100001:
                if 0 <= next_r and not visited[next_r]:
                    queue.append((next_r,cur_len+1))
                    visited[next_r] = True

    return -1

print(bfs(N, K))

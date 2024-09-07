"""
BFS 문제! 시간복잡도 : O(노드수 + 간선 수) = O(N)
"""
from collections import deque

N, K = map(int, input().split(' '))

answer = 0

def bfs(n, t):
    visited = [False for _ in range(100001)]
    visited[n] = True
    queue = deque()
    queue.append((n, t))

    while queue:
        cur_r, time = queue.popleft()
        if cur_r == K:
            return time
        for i in (cur_r * 2, cur_r - 1, cur_r + 1):
            if 0 <= i < 100001 and visited[i] == False:
                if i == (cur_r * 2):
                    queue.append((i, time))
                    visited[i] = True
                else:
                    queue.append((i, time+1))
                    visited[i] = True

print(bfs(N, 0))

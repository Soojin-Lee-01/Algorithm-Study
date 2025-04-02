"""
BFS로 풀이
시간복잡도 : O(F)
"""

from collections import deque

F, S, G, U, D = map(int, input().split())

def dfs(n):
    queue = deque()
    queue.append((n, 1))

    visited[n] = True
    while queue:
        cur, len = queue.popleft()
        for x in (U, -D):
            next = cur + x
            if next == G:
                return len
            if 1 <= next < F:
                if not visited[next]:
                    queue.append((next, len + 1))
                    visited[next] = True

    return -1


visited = [False  for _ in range(0, F+1)]

if G == S:
    print(0)
else:
    answer = dfs(S)
    if answer == -1:
        print("use the stairs")
    else:
        print(answer)

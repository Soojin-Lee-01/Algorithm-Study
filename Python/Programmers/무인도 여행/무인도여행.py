"""
시간복잡도 : O(N**2)
BFS로 풀이
"""

from collections import deque

def bfs(graph, r, c, visited):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    count = graph[r][c]
    while queue:
        cur_r, cur_c = queue.popleft()
        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < len(graph) and 0 <= next_c < len(graph[0]):
                if not visited[next_r][next_c]:
                    if type(graph[next_r][next_c]) == int:
                        count += graph[next_r][next_c]
                        queue.append((next_r, next_c))
                        visited[next_r][next_c] = True
    return count
                        
def solution(maps):
    answer = []
    graph = []
    for i in range(len(maps)):
        data = []
        for j in range(len(maps[0])):
            if maps[i][j].isdigit():
                data.append(int(maps[i][j]))
            else:
                data.append(maps[i][j])
        graph.append(data)
        
    visited = [[False for _ in range(len(maps[0])) ] for _ in range(len(maps))]
    
    answer = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if type(graph[i][j]) == int and not visited[i][j]:
                answer.append(bfs(graph, i, j, visited))
                    
    return sorted(answer) if answer else [-1]

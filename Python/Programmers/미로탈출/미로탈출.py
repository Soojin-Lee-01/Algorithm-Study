from collections import deque
def solution(maps):
    def bfs(r, c, target_x, target_y):
        queue = deque()
        queue.append((r, c, 0))
        visited[r][c] = True
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            cur_r, cur_c, cur_len = queue.popleft()
            if cur_r == target_x and cur_c == target_y:
                return cur_len
            for dr, dc in directions:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if 0 <= next_r < len(maps) and 0 <= next_c < len(maps[0]):
                    if not visited[next_r][next_c]:
                        if maps[next_r][next_c] != 'X':
                            queue.append((next_r, next_c, cur_len + 1))
                            visited[next_r][next_c] = True
        return -1
    answer = 0
    start = []
    labor = []
    end = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = [i, j]
            if maps[i][j] == 'L':
                labor = [i, j]
            if maps[i][j] == 'E':
                end = [i, j]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    first = bfs(start[0], start[1], labor[0], labor[1])
    if first == -1:
        return -1
    answer += first
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    two = bfs(labor[0], labor[1], end[0], end[1])
    if two == -1:
        return -1
    answer += two
    
    
    return answer

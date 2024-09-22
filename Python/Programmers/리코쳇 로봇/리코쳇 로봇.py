from collections import deque

def solution(board):
    answer = 0
    start = None
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i, j)
                
    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        visited[r][c] = 1
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        while queue:
            cur_r, cur_c = queue.popleft()
            
            if board[cur_r][cur_c] == 'G':
                return visited[cur_r][cur_c] - 1
            
            for dr, dc in directions:
                next_r = cur_r
                next_c = cur_c
                
                while True:
                    new_r = next_r + dr
                    new_c = next_c + dc
                    
                    if not (0 <= new_r < len(board)) or not(0 <= new_c < len(board[0])) or board[new_r][new_c] == 'D':
                        break
                        
                    next_r = new_r
                    next_c = new_c
                    
                if not visited[next_r][next_c]:
                    visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                    queue.append((next_r, next_c))
                    
        return -1
    
    return bfs(start[0], start[1])

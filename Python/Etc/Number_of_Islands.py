from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def bfs(r, c):
            visited[r][c] = True
            queue = deque()
            queue.append((r, c))

            directions = [(1, 0),(0, 1), (0, -1),(-1, 0)]

            while queue:
                cur_r, cur_c = queue.popleft()
               
                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc
                    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                        if not visited[next_r][next_c]:
                            if grid[next_r][next_c] == '1':
                                queue.append((next_r, next_c))
                                visited[next_r][next_c] = True
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    bfs(i, j)
                    answer += 1

        return answer

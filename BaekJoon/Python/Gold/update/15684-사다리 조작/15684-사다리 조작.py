n, m, h = map(int, input().split())

pos = []

graph = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1


for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0 and (j == 0 or graph[i][j-1] == 0) and (j == n-1 or graph[i][j+1] == 0):
            pos.append((i, j))

def check():
    for start in range(n):
        cur_c = start
        for cur_r in range(h):
            if cur_c < n-1 and graph[cur_r][cur_c] == 1:
                cur_c += 1
            elif cur_c > 0 and graph[cur_r][cur_c-1] == 1:
                cur_c -= 1
        if cur_c != start:
            return False
    return True

def dfs(s, temp):
    if s == cnt:
        return check()

    for j in range(temp, len(pos)):
        x, y = pos[j]
        if graph[x][y] == 0 and (y == 0 or graph[x][y-1] == 0) and (y == n-1 or graph[x][y+1] == 0):
            graph[x][y] = 1
            if dfs(s+1, j+1) is True:
                return True
            graph[x][y] = 0

    return False

ans = 0
for cnt in range(4):
    if dfs(0, 0):
        ans = cnt
        break
else:
    ans = -1

print(ans)

def bfs(r, c, n, temp =[]):
    global count
    if n == 7:
        answer.add(tuple(temp))

        return

    for dr, dc in directions:
        cur_r = dr + r
        cur_c = dc + c
        if 0 <= cur_r < len(graph) and 0 <= cur_c < len(graph[0]):
            temp.append((graph[cur_r][cur_c]))
            bfs(cur_r, cur_c, n+1, temp)
            temp.pop()
          
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
count = 0

n = int(input())

for t in range(n):
    graph = []
    for m in range(4):
        data = list(map(int, input().split()))
        graph.append(data)
    answer = set()

    for i in range(len(graph)):
        for j in range(len(graph)):
            bfs(i, j, 0)

    print(f'#{t+1} {len(answer)}')

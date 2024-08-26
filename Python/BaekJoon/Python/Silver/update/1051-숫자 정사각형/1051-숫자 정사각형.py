def square(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if graph[i][j] == graph[i][j+s-1] == graph[i+s-1][j] == graph[i+s-1][j+s-1]:
                return True
    return False


n, m = map(int, input().split(' '))
graph = []

for i in range(n):
    data = list(map(int, input().rstrip()))
    graph.append(data)

size = min(n, m)

for i in range(size, 0, -1):
    if square(i) is True:
        print(i**2)
        break
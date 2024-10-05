N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))

temp = []

def dfs(start):
    if len(temp) == M:
        print(*temp)
        return
    for i in range(start, len(data)):
        if data[i] not in temp:
            temp.append(data[i])
            dfs(i+1)
            temp.pop()

dfs(0)

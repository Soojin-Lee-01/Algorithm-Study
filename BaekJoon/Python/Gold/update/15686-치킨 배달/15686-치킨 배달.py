import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []

chicken = [] # 치킨 집 좌표
house = [] # 집 좌표

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(data)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

def combina(lst, num):
    result = []
    if num > len(lst):
        return result
    if num == 1:
        for i in lst:
            result.append([i])
    elif num > 1:
        for i in range(len(lst)-num+1):
            for temp in combina(lst[i+1:], num-1):
                result.append([lst[i]] + temp)
    return result

min_value = int(1e9)

def find_dis(c):
    global min_value
    all_c = 0
    for h_x, h_y in house:
        min_c = 2 * n + 1
        for c_x, c_y in c:
            dist = (abs(h_x-c_x) + abs(h_y-c_y))
            min_c = min(min_c, dist)

        all_c += min_c
    min_value = min(min_value, all_c)

for c in combina(chicken, m):
    find_dis(c)

print(min_value)




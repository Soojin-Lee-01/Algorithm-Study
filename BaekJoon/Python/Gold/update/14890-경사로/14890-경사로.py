N, L = map(int, input().split())

graph = []

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

def solution(t, visi, a):
    for i in range(len(t)-1):
        if abs(t[i]-t[i+1]) == 1:
            """
            1. 오른쪽이 왼쪽보다 더 작을 때
            2. 왼쪽이 오른쪽보다 더 작을 때
            """
            if (t[i] > t[i+1]):
                cur = t[i+1]
                route = []
                for j in range(i+1,len(t)):
                    if len(route) == L:
                        for dr, dc in route:
                            if visi[dr][dc] is True:
                                return False
                            else:
                                visi[dr][dc] = True
                        break
                    elif t[j] == cur:
                        route.append((a, j))
                    else:
                        return False
                if len(route) < L:
                    return False
            elif (t[i] < t[i+1]):
                cur = t[i]
                route = []
                for j in range(i, -1, -1):
                    if len(route) == L:
                        for dr, dc in route:
                            if visi[dr][dc] is True:
                                return False
                            else:
                                visi[dr][dc] = True
                        break
                    elif t[j] == cur:
                        route.append((a, j))
                    else:
                        return False
                if len(route) < L:
                    return False

        elif abs(t[i]-t[i+1]) > 1:
            return False

    return True


def solve(gra):
    result = 0
    for i in range(N):
        visited = [[False for _ in range(N)] for _ in range(N)]
        temp = gra[i]
        if solution(temp, visited, i) is True:
            result += 1

    return result


final = 0

final += solve(graph)
t_g = list(map(list, zip(*graph)))
final += solve(t_g)


print(final)

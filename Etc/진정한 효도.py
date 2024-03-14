"""
세 숫자를 조정하여 그 차이의 절대값을 취한 후 모두 더함 -> 조정량의 총 합
숫자들을 모두 더하고 -> 가장 작은값을 제거 -> 가장 큰값이 균형값
"""

import sys

graph = []

for i in range(3):
    data = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(data)


def func(a, b, c):
    value = a + b + c - min(a, b, c) - max(a, b, c)
    return abs(value - a) + abs(value - b) + abs(value - c)


result1 = []
result2 = []
while True:
    for i in range(3):
        a = graph[i][0]
        b = graph[i][1]
        c = graph[i][2]
        temp = func(a, b, c)
        result1.append(temp)
    for i in result1:
        if i == 0:
            print(0)
            exit()

    for i in range(3):
        test = []
        for j in range(3):
            test.append(graph[j][i])
        temp = func(test[0], test[1], test[2])
        result2.append(temp)

    for i in result2:
        if i == 0:
            print(0)
            exit()

    result1_min = min(result1)
    result2_min = min(result2)
    if result2_min < result1_min:
        print(result2_min)
    else:
        print(result1_min)
    exit()
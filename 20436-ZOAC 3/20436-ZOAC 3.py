import sys

# solution - 1

L, R = map(str, sys.stdin.readline().rstrip().split(' '))

graph = {'q' : [0, 0], 'w': [0, 1], "e" : [0, 2], "r" : [0, 3], "t": [0, 4], "y" : [0, 5], "u" :[0, 6], "i" : [0, 7], 'o' : [0, 8], "p" :[0, 9],
         "a" : [1, 0], 's' : [1, 1], 'd': [1, 2], 'f': [1, 3], 'g' : [1, 4], 'h' : [1, 5], "j" : [1, 6], "k" : [1, 7], 'l' : [1, 8],
         'z' : [2, 0], 'x': [2, 1], 'c' : [2, 2], 'v' : [2, 3], 'b' : [2, 4] , 'n' : [2, 5], 'm' : [2, 6]}

word = list(map(str, sys.stdin.readline().rstrip()))

def simu(list, l, r):
    R_x = 0
    R_y = 0
    L_x = 0
    L_y = 0
    result = 0
    for i in list:
        if i in "qwertasdfgzxcv": # 왼손일 경우
            if l != 0:
                data = abs(graph[l][0] - graph[i][0]) + abs(graph[l][1] - graph[i][1])
                result += data
                result += 1
                l = 0
                L_x = graph[i][0]
                L_y = graph[i][1]
            else:
                data = abs(L_x - graph[i][0]) + abs(L_y - graph[i][1])
                result += data
                result += 1
                L_x = graph[i][0]
                L_y = graph[i][1]
        else: # 오른손일 경우
            if r != 0:
                data = abs(graph[r][0] - graph[i][0]) + abs(graph[r][1] - graph[i][1])
                result += data
                result += 1
                r = 0
                R_x = graph[i][0]
                R_y = graph[i][1]
            else:
                data = abs(R_x - graph[i][0]) + abs(R_y - graph[i][1])
                result += data
                result += 1
                R_x = graph[i][0]
                R_y = graph[i][1]

    return result
print(simu(word,L, R))


# Solution - 2

keyboard = [["q", "w", "e", "r", "t","y", "u", "i", "o", "p"], ["a", "s", "d", "f", "g","h", "j", "k", "l"],
       ["z", "x","c", "v","b", "n", "m"]]

def find_location(s, keyboard):
    for i , key in enumerate(keyboard):
        if s in key:
            return i, key.index(s)
    return None

L, R = map(str, sys.stdin.readline().rstrip().split(' '))


L_x, L_y = find_location(L, keyboard)
R_x, R_y = find_location(R, keyboard)
result_key = 0
for i in input():
    x, y = find_location(i, keyboard)
    if i in "qwertasdfgzxcv":
        result_key += abs(L_x - x) + abs(L_y - y)
        L_x = x
        L_y = y
        result_key += 1
    else:
        result_key += abs(R_x - x) + abs(R_y - y)
        R_x = x
        R_y = y
        result_key += 1

print(result_key, end='')



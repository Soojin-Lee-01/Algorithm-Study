# PCCP 1회 모의고사 - 2번 문제

# Solution - 1

result = 0

def dfs(n, m, check, ability):
    global result
    temp = len(ability[0])
    
    if n == temp:
        result = max(result, m)
    else:
        for i in range(len(ability)):
            if check[i] == 0:
                check[i] = 1
                dfs(n+1, m + ability[i][n], check, ability)
                check[i] = 0

def solution(ability):
    check = [0] * len(ability)
    dfs(0, 0, check, ability)
    return result

# Solution -2

from itertools import permutations

def solution(ability):
    num_people = len(ability)
    num_tasks = len(ability[0])
    max_score = 0

    for perm in permutations(range(num_people), num_tasks):
        temp_score = 0
        for task in range(num_tasks):
            temp_score += ability[perm[task]][task]
        max_score = max(max_score, temp_score)
    
    return max_score
    

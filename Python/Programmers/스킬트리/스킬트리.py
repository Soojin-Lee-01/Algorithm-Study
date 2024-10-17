def temp(n, skill):
    target = 0
    for i in range(len(n)):
        if n[i] in skill:
            if n[i] == skill[target]:
                target += 1
            else:
                return False
    return True

def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for n in skill_trees:
        if temp(n, skill):
            answer += 1
                
    return answer

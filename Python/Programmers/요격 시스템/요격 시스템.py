def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: (x[1], x[0]))
    current = 0
    
    # 요걱한 기준을 잘 생각해보자! 서로 비교해서 크거나 같으면 요걱 +1, 아니면 요격 x
    for target in targets:
        if target[0] >= current:
            answer += 1
            current = target[1]
        
    return answer

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    temp = [i for i in range(1, n+1)]
    datas = list(combinations(temp, 5))
    
    # 갯수와 일치하는지 확인
    def check(target):
        for t in range(len(q)):
            count = 0
            for k in range(len(q[t])):
                for m in range(len(target)):
                    if q[t][k] == target[m]:
                        count += 1
            if count != ans[t]:
                return False
        return True
    
    for i in datas:
        temp = i
        if check(temp): answer += 1
    
    return answer

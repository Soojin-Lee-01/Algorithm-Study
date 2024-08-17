def solution(keymap, targets):
    dic = {}
    
    for i in range(len(keymap)):
        temp = keymap[i]
        for j in range(len(temp)):
            if temp[j] not in dic:
                dic[temp[j]] = j+1
            elif temp[j] in dic:
                dic[temp[j]] = min(dic[temp[j]], j+1)
                
    answer = []
    
    for i in range(len(targets)):
        temp = targets[i]
        final = 0
        che = 0
        for j in range(len(temp)):
            if temp[j] not in dic:
                final = -1
                break
            elif temp[j] in dic:
                final += dic[temp[j]]
        if che == 0:
            answer.append(final)
                    
    return answer

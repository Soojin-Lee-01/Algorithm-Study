def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    temp = []
    for a, b in dic.items():
        temp.append((a, b))
    temp = sorted(temp, key=lambda x: (-x[1], x[0]))
    stack = []
    for a, b in temp:
        for i in range(b):
            if len(stack) < k:
                stack.append(a)
            else:
                break

    return len(set(stack))


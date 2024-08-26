def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    temp = []
    for i in s:
        temp.append(i.split(','))
    temp.sort(key=len)
    for i in temp:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
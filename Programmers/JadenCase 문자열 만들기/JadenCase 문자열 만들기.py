def solution(s):
    answer = ''
    temp = list(map(str, s.split(' ')))
    result = []
    for i in temp:
        i = i.lower()
        result.append(i.capitalize())
        result.append(' ')
    result.pop()
    answer = ''.join(map(str, result))

    return answer
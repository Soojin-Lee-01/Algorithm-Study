def solution(s):
    temp = s
    result = [0, 0]
    while temp != '1':
        for i in range(len(temp)):
            if temp[i] == '0':
                result[1] += 1
        temp = temp.replace('0', '')
        result[0] += 1
        temp = str(format(len(temp), 'b'))
    return result
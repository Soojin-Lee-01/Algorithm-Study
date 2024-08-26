# PCCP 모의고사 1회  - 1번
def solution(input_string):
    dic = {}
    temp = ""
    result = set()

    for char in input_string:
        if char not in dic:
            dic[char] = 1
            temp = char
        else:
            if temp != char:
                temp = char
                result.add(char)
    
    sorted_result = sorted(result)
    return ''.join(sorted_result) if sorted_result else "N"

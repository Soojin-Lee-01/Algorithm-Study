def solution(want, number, discount):
    answer = 0
    temp = []
    for i in range(len(want)):
        temp.extend([want[i]] * number[i])
    temp = sorted(temp)

    for i in range(len(discount)-9):
        temp_final = discount[i:i+10]
        if temp == sorted(temp_final):
            answer += 1

    return answer
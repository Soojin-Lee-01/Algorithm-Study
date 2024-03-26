def solution(participant, completion):
    number = {}
    for i in participant:
        if i in number:
            number[i] += 1
        else:
            number[i] = 1
    for i in completion:
        number[i] -=1
    for key, value in number.items():
        if value == 1:
            return key
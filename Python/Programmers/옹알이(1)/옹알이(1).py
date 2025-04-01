def solution(babbling):
    answer = 0
    
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya", "1")
        babbling[i] = babbling[i].replace("ye", "2")
        babbling[i] = babbling[i].replace("woo", "3")
        babbling[i] = babbling[i].replace("ma", "4")
    for n in babbling:
        if n.isdigit():
            answer += 1
            
    return answer

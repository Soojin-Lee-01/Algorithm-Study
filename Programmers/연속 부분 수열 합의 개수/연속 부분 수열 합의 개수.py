def solution(elements):
    answer = 0
    numberSet = set() # 중복을 담지 않기 위해서

    elementLen = len(elements)
    elements = elements * 2 # 배열을 늘려줌

    for i in range(elementLen):
        for j in range(elementLen):
            # 순서대로 더해줌
            numberSet.add(sum(elements[j:j+i+1]))
    # 담겨져있는 개수를 반환함
    answer = len(numberSet)
    return answer


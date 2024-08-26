def solution(numbers):
    result = [-1] * len(numbers)  # 결과 리스트를 -1로 초기화
    stack = []  # 인덱스를 저장할 스택

    for i in range(len(numbers)):
        # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 숫자보다 큰 경우
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        # 현재 인덱스를 스택에 추가
        stack.append(i)

    return result

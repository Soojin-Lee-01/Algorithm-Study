def solution(n):
    number = n
    temp = list(bin(n)).count('1') # 2진수로 변환하여 1을 카운트
    while True:
        number += 1 # 숫자를 증가
        # 증가한 숫자의 2진수 변환 1의 개수와 원래 수의 2진수 변환 1의 개수가 같다면
        if temp == list(bin(number)).count('1'):
            return number
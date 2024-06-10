def solution(n, a, b): # 아래에서부터 위로 대진 횟수를 구한다.
    round  = 0
    while a != b:
        round += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    return round
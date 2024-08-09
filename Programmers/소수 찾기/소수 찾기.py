from itertools import permutations
def final(num):
    for i in range(2, num):
        if num % i == 0:
            # 소수가 아니다.
            return False
    # 소수다
    return True
def solution(numbers):
     
    answer = set()
    data = list(numbers.rstrip(""))
    for k in range(1, len(numbers)+1):
        combo = list(permutations(data, k))
        for m in range(len(combo)):
            temp = int(''.join(map(str, combo[m])))
            if temp != 1 and temp != 0:
                if final(temp):
        
                    answer.add(temp)
    return len(answer)

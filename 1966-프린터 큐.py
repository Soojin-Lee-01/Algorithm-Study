from collections import deque
import sys

def solution(a, m):
    a = deque([(idx, val) for idx, val in enumerate(a)])
    count = 0 # 출력한 문서의 수

    while True:
        cur = a.popleft()
        if any(cur[1] < x[1] for x in a):
            a.append(cur)
        else:
            count += 1
            if cur[0] == m:
                return count

num = int(sys.stdin.readline()) # 테스트 케이스의 개수

for i in range(num):
    n, m = map(int, sys.stdin.readline().split()) # 문서 개수, 타겟의 인덱스
    importa = list(map(int, sys.stdin.readline().split())) # 문서의 중요도
    result = solution(importa, m)
    print(result)

"""
any() 내장함수 - True, False 반환

# numbers 리스트에서 홀수가 하나라도 있는지 확인
numbers = [1, 2, 3, 4, 5]
result = any(x % 2 == 1 for x in numbers)
print(result)

# 문자열 리스트에서 길이가 5인 문자열이 하나라도 있는지 확인
words = ["apple", "banana", "cherry", "date"]
result = any(len(words) == 5 for word in words)
print(result)

# 빈 리스트에서 any() 함수 사용
empty_list = []
result = any(empty_list)
print(result) # False 출력

"""




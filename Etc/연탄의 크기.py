"""
j값을 잘 설정해주는게 필요!!

- 전역변수
함수안에서 전역변수를 선언할때 global로 선언해준다.
함수 밖에 선언된 변수는 함수 내부에서 읽을 수는 있지만 새로운 값을 할당할수는 없다!

ex) 가능한 예제
result = 0
def solve():
print(result)
"""

import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rstrip().split(' ')))

number = 2
result = 0
def solution(b):
    temp = 0
    global result
    if result == n:
        print(result)
        exit()
    else:
        for i in data:
            if i % b == 0:
                temp += 1
    result = max(result, temp)
if n == 1:
    result = 1
else:
    for j in range(2, max(data)+1):
        solution(j)

print(result)

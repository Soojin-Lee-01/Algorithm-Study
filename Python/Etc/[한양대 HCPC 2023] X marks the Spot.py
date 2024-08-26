"""
result = ''로 두고 += 하는 방법은 매번 새로운 문자를 생성하고 이어 붙이는 작업을 수행하게 됨
result = [] 리스트에 추가하고 나중에 합치는 방법은 위의 시간을 줄여줌
<문자열 조작이 반복적으로 이어지는 경우 리스트에 값을 추가하고 마지막에 join을 사용하는게 성능적으로 유리함>
"""

import sys

n = int(sys.stdin.readline().rstrip())

result = []

for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    index = 0

    if 'x' in a:
        index = a.index('x')
    elif 'X' in a:
        index = a.index('X')

    result.append(b[index])

print(''.join(result).upper())
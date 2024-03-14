"""
pop(0) -> O(n)
pop() - > O(1)

이유는?
pop(0)은 맨 앞의 요소를 제거하고 한칸씩 앞으로 땡겨줘야한다!
pop()은 그냥 맨 뒤의 요소를 제거해준다.
"""

import sys

w, n = map(int, sys.stdin.readline().split(' '))

items = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    items.append((a, b))

items.sort(key=lambda x: x[1], reverse=True) # 두번째 요소를 기준으로 내림차순

result = 0

for weight, value in items:
    if w >= weight:
        result += weight * value
        w -= weight
    else:
        result += w * value
        break

print(result)
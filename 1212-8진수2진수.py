import sys

n = str(sys.stdin.readline())
o = int(n, 8)
print(format(o, 'b'))

"""
<Python 진수 변환>
1. 10진수에서 2진수, 8진수, 16진수 변환
solution 1)bin(), oct(), hex() 내장함수를 사용
solution 2) format() 내장함수 사용
ex)
value = 60
b = format(value, '#b') : 접두어가 있는 결과
b = format(value, 'b') : 접두어가 빠진 결과

2. 다른 진수에서 10진수로 변환
2진수, 8진수, 18진수
ex)
b = int('0b111100', 2)
o = int('0o74', 8)
h = int('0x3c', 16)
"""
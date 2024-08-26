"""
DP를 활용한 문제!
메모리 계산을 위해서 리스트의 길이가 최대 n 이므로
n * 4바이트로 계산
1MB - > 1024KB
"""

import sys

n = int(sys.stdin.readline())

mem = [0] * (n+1)

mem[0] = 2

for i in range(1, n+1):
    mem[i] = mem[i-1] + 2**(i-1)

print(mem[n] * mem[n])
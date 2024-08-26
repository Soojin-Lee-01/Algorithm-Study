"""
mem 메모리 관리를 위해서 % 1000000007을 해주고 저장해주는 것이 좋다!
시간복잡도 -> O(n)
"""
import sys

k, p, n = map(int, sys.stdin.readline().rstrip().split(' '))

mem = {}

for i in range(n):
    mem[i+1] = 0
mem[1] = k * p % 1000000007
if p == 1:
    print(mem[1] % 1000000007)
else:
    for i in range(2, n+1):
        mem[i] = mem[i-1] * p % 1000000007
    print(mem[n])
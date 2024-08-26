"""
포함되어있는지 확인할때!!!
문자열로 바꾸어 비교해본다!!!!!!!!!!!!!
시간복잡도 : O(n)
"""

import sys

m, n, k = map(int, sys.stdin.readline().split(' '))

if m > n :
    print("normal")
    exit()

corret = "".join(list(map(str,sys.stdin.readline().rstrip().split())))
input = "".join(list(map(str,sys.stdin.readline().rstrip().split())))

if corret in input:
    print("secret")
else:
    print("normal")
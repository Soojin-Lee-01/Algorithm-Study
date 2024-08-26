"""
1부터 8까지 숫자가 무조건 한번씩 등장하므로 sorted()사용가능!!
시간복잡도 : O(n)
"""

import sys

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

if numbers == sorted(numbers):
    print("ascending")
elif numbers == sorted(numbers, reverse=True):
    print("descending")
else:
    print("mixed")
import sys

n = int(sys.stdin.readline())

word = [sys.stdin.readline().rstrip() for  i in range(n)]

word = list(set(word))

word.sort()
word.sort(key=len)

for i in word:
    print(i)

"""
메모리 사용 측면 효율
sort() > sorted()
"""
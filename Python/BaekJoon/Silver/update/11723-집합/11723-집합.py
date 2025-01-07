"""
시간 복잡도 비교
<list vs set>
삽입 : O(1) vs O(1)
삭제 : O(N) vs O(1)
검색 : O(N) vs O(1)
전체 순회 : O(N) vs O(N)
"""

import sys

N = int(sys.stdin.readline())

answer = set()
temp = set(range(1, 21))
for _ in range(N):
    data = list(map(str, sys.stdin.readline().split()))
    if data[0] == "add":
        answer.add(int(data[1]))
    elif data[0] == "remove":
        if int(data[1]) in answer:
            answer.remove(int(data[1]))
    elif data[0] == "check":
        if int(data[1]) in answer:
            print(1)
        else:
            print(0)
    elif data[0] == "toggle":
        if int(data[1]) in answer:
            answer.remove(int(data[1]))
        else:
            answer.add(int(data[1]))
    elif data[0] == "all":
        answer = temp.copy()
    else:
        answer = set()

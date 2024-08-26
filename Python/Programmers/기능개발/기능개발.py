"""
파이썬 -> / : float, // : int
-((p-100)//s) -> 이용해서 ceil을 대신할 수 있음..
"""


def solution(progresses, speeds):
    stack = []
    for i in range(len(speeds)):
        a = -((progresses[i] - 100) // speeds[i])
        stack.append(a)
    stack = stack[::-1]
    result = []
    final = []
    for i in range(len(stack)):
        if len(result) == 0:
            result.append([stack.pop(), 1])
        else:
            if result[len(result) - 1][0] >= stack[len(stack) - 1]:
                stack.pop()
                result[len(result) - 1][1] += 1
            else:

                result.append([stack.pop(), 1])
    for i in range(len(result)):
        final.append(result[i][1])
    return final






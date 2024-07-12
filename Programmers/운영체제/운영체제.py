# PCCP 모의고사 1회 - 4번 문제

import heapq

def solution(program):
    answer = [0] * 11
    program = sorted(program, key=lambda x: (x[1]))
    heap = []
    cur = 0

    def call_program():
        while len(program) > 0 and program[0][1] <= cur:
            heapq.heappush(heap, program.pop(0))

    while len(program) > 0 or not len(heap) == 0:
        if len(heap) == 0:
            cur = program[0][1]
            call_program()
        exe = heapq.heappop(heap)
        answer[exe[0]] += (cur - exe[1])
        cur += exe[2]
        call_program()

    answer[0] += cur

    return answer

solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]])

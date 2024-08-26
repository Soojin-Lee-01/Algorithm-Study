# PCCP 모의고사 1회 - 3번

def solution(queries):
    answer = []

    def sol(n, p):
        if n == 1:
            return "Rr"
        prev = sol(n-1, (p-1)//4+1)

        if prev != "Rr":
            return prev
        lst = ["RR", "Rr", "Rr", "rr"]
        return lst[p%4-1]

    for n, p in queries:
        answer.append(sol(n, p))
    return answer

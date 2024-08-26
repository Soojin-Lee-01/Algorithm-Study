def solution(n, lost, reserve):
    temp_lost = set(lost) - set(reserve)
    temp_reserve = set(reserve) - set(lost)

    for i in temp_reserve:
        if i - 1 in temp_lost:
            temp_lost.remove(i - 1)
        elif i + 1 in temp_lost:
            temp_lost.remove(i + 1)

    return n - len(temp_lost)
def solution(diffs, times, limit):
    num = [i for i in range(1, max(diffs)+1)]
    left = 0
    right = len(num) -1
    answer = 10e12
    while (left <= right):
        mid_num = (left + right) // 2
        mid = num[mid_num]
        temp = 0
        for j in range(len(diffs)):
            if diffs[j] <= mid:
                temp += times[j]
            else:
                temp += ((times[j-1] + times[j]) * (diffs[j] - mid)) + times[j]
        
        if temp <= limit:
            right = mid_num - 1
            answer = min(answer, num[mid_num])
        else:
            left = mid_num + 1
    return answer

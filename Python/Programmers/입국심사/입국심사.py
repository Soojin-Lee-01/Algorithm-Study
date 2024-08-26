"""
이분 탐색 : 발생하는 시간을 기준으로 이분 탐색을 실시한다!
"""

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    mid = (left + right) // 2
    
    while left <= right:
        mid = (left + right) // 2
        person = 0
        for time in times:
            person += (mid // time)
        if person >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

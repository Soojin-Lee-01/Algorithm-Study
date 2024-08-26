"""
입력의 사이즈가 너무 커서, 완전탐색이 아니라고 판단하면! 이분탐색을 시도해보자!!
"""
def solution(distance, rocks, n):
    left = 1
    right = distance
    
    rocks = sorted(rocks)
    rocks.append(distance)
    
    while left <= right:
        mid = (left+right) //2
        remove = 0
        prev = 0
        
        for v in rocks:
            dist = v - prev
            if dist < mid:
                remove += 1
                if remove > n:
                    break
                
            else:
                prev = v
                
        if remove > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer
                    

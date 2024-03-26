def solution(nums):
    result = []
    for i in nums:
        if len(result) < len(nums) / 2:
            if i in result:
                pass
            else:
                result.append(i)

    answer = len(result)
    return answer
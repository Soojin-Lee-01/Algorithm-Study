def solution(arr):
    result = []
    for i in range(len(arr)):
        if len(result) > 0:
            if result[len(result) - 1] != arr[i]:
                result.append(arr[i])
        else:
            result.append(arr[i])
    return result


def solution(count, data):
    for _ in range(count):
        max_data = [float('-inf'), 0]
        min_data = [float('inf'), 0]
        for i in range(len(data)):
            if data[i] > max_data[0]:
                max_data[0] = data[i]
                max_data[1] = i
            if data[i] < min_data[0]:
                min_data[0] = data[i]
                min_data[1] = i
        if data[max_data[1]]-1 == data[min_data[1]]:
            return 1
        data[min_data[1]] += 1
        data[max_data[1]] -= 1

    return max(data) - min(data)

for j in range(10):

    count = int(input())
    data = list(map(int, input().split()))

    answer = solution(count, data)
    print(f'#{j+1} {answer}')

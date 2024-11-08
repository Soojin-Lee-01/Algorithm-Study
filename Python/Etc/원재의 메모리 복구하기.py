test = int(input())

for i in range(test):
    data = list(input())

    for k in range(len(data)):
        data[k] = int(data[k])
    first = [0 for _ in range(len(data))]

    pointer = 0
    answer = 0
    while (pointer < len(data)):
        if data[pointer] != first[pointer]:
            answer += 1
            temp = data[pointer]
            for j in range(pointer, len(data)):
                first[j] = temp
        pointer += 1

    print(f'#{i+1} {answer}')

test = int(input())

for i in range(test):
    n = int(input())
    data = list(map(int, input().split()))
    answer = set()
    answer.add(0)

    for j in data:
        new_set = set()
        for k in answer:
            new_set.add(j+k)
        answer = answer | new_set


    print(f'#{i+1} {len(answer)}')

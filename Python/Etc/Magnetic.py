for i in range(10):
    graph = []
    n = int(input())
    for _ in range(100):
        data = list(map(int, input().split()))
        graph.append(data)

    answer = 0

    for a in range(100):
        check = 0
        for b in range(100):
            if graph[b][a] == 1:
                check += 1
            elif graph[b][a] == 2:
                if check >= 1:
                    answer += 1
                    check = 0

    print(f'#{i+1} {answer}')

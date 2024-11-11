def row_col_sum(gra):
    global answer
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += gra[i][j]
        answer = max(answer, temp)

def diagonal(gra):
    global answer
    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += gra[i][i]
    answer = max(answer, diagonal_sum)

for i in range(10):
    n = int(input())
    graph = []
    for _ in range(100):
        data = list(map(int, input().split()))
        graph.append(data)

    answer = -1
    row_col_sum(graph)
    diagonal(graph)

    temp_graph = list(map(list, zip(*graph[::-1])))

    row_col_sum(temp_graph)
    diagonal(temp_graph)

    print(f'#{i+1} {answer}')

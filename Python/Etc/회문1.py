def calculate(gra):
    global answer
    for j in range(8):
        temp = gra[j]
        for m in range(len(temp)-n+1):
            te = temp[m:m+n]
            if len(te) % 2 == 0:
                a = te[:len(te)//2]
                b = te[len(te)//2:][::-1]

                if a == b:
                    answer += 1
            else:
                a = te[:len(te)//2]
                b = te[len(te)//2+1:][::-1]

                if a == b:
                    answer += 1

for i in range(10):
    n = int(input())
    graph =[]
    answer = 0
    for _ in range(8):
        data = list(input())
        graph.append(data)

    calculate(graph)

    temp_graph = list(map(list, zip(*graph[::-1])))

    calculate(temp_graph)
    print(f'#{i+1} {answer}')

def solution(gra, n):
    temp_answer = 1
    for k in range(len(gra)):
        temp = gra[k]
        for j in range(len(temp)-n+1):
            if temp[j:j+n] == temp[j:j+n][::-1]:
                return True
 
    return False
 
for _ in range(10):
    t = int(input())
    graph = []
 
    for _ in range(100):
        data = list(input())
        graph.append(data)
 
    answer = 1
    for i in range(2, 101):
        if solution(graph, i):
            answer = i
 
    temp_graph = list(map(list, zip(*graph)))
 
    for i in range(answer, 101):
        if solution(temp_graph, i):
            answer = i
 
    print(f'#{t} {answer}')

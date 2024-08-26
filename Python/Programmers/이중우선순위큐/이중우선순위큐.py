import heapq

def solution(operations):
    data1 = []
    
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            heapq.heappush(data1, int(operations[i][2:]))
        elif operations[i] == 'D 1':
            if len(data1) > 0:
                data1.sort()
                data1.pop()
        elif operations[i] == 'D -1':
            if len(data1) > 0:
                heapq.heappop(data1)

    if len(data1) == 0:
        return [0, 0]
    else:
        return[max(data1), min(data1)]

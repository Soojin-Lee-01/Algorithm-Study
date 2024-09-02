import heapq

def solution(scoville, K):
    data = [] 
    for i in range(len(scoville)):
        heapq.heappush(data, scoville[i])
    answer = 0
    while True:
        if data[0] >= K:
            break
        if len(data) >= 2:
            a = heapq.heappop(data)
            b = heapq.heappop(data)
            temp = a + (b * 2)
            heapq.heappush(data, temp)
        else:
            answer = -1
            break
        answer += 1
                
    return answer

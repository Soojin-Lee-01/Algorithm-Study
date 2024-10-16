import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    else:
        heap = []
        for i in works:
            heapq.heappush(heap, -1 * i)

        for i in range(n):
            temp = heapq.heappop(heap)
            temp += 1
            heapq.heappush(heap, temp)
        answer = 0

        for i in range(len(heap)):
            answer += ((-1 * heap[i]) ** 2)
        return answer

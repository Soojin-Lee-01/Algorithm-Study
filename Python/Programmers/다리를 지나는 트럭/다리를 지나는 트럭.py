from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    current = 0
    while bridge:
        answer += 1
        current -= bridge.popleft()
        if truck_weights:
            if current + truck_weights[0] <= weight:
                current += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer

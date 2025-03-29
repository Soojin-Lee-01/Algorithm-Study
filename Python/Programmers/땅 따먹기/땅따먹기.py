"""
시간복잡도 : O(N)
"""
def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for k in range(4):
            temp = land[i][k]
            for j in range(4):
                if k != j:
                    land[i][k] = max(land[i][k], temp + land[i-1][j])
    
    return max(land[len(land)-1])

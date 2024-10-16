def solution(dirs):
    # 위 아래 오른쪽 왼쪽
    directions = {'U' : [0, 1], 'D' : [0, -1], 'R' : [1, 0] , 'L' : [-1, 0]}
    answer = 0
    x = y = 0
    diret = 0
    visited = []
    
    for i in range(len(dirs)):
        n = dirs[i]    
        
        next_r = x + directions[n][0]
        next_c = y + directions[n][1]
        
        if -5 <= next_r <= 5 and -5 <= next_c <= 5:
            if (x, y, next_r, next_c) not in visited and (next_r, next_c, x, y) not in visited:
                answer += 1
                visited.append((x, y, next_r, next_c))
                visited.append((next_r, next_c, x, y))
            x = next_r
            y = next_c
            
    return answer

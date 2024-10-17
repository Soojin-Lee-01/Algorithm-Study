from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        cur_r, cur_len = queue.popleft()
        if cur_r == target:
            return cur_len
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[i] != cur_r[i]:
                    count += 1
            
            if count == 1:
                queue.append((word, cur_len + 1))
                    
    return 0
                
def solution(begin, target, words):

    if target not in words:
        return 0
    
    final = bfs(begin, target, words)
    
    return final

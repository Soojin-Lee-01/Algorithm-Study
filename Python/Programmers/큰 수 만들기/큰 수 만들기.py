def solution(number, k):
    stack = []
    
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    
    while k > 0:
        stack.pop()
        k -= 1
        
    return ''.join(map(str, stack))

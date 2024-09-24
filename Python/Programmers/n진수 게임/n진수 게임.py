def solution(n, t, m, p):
    answer = ''
    data = []
    
    def solve(num, base):
        rev_base = ''
        digits = "0123456789ABCDEF" 
        
        while num > 0:
            num, mod = divmod(num, base)
            rev_base += digits[mod] 
            
        return rev_base[::-1] if rev_base else '0'
    
    for i in range((t * m) + 1):
        num = solve(i, n) 
        data.extend(num) 
    
    for i in range(p-1, t*m, m):
        answer += data[i]
    
    return answer

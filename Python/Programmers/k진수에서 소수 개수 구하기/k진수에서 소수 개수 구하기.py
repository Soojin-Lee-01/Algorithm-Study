import math

def number(n, k):
    temp = ""
    
    while (n > 0):
        temp = str(n % k) + temp
        n = n // k
    
    return temp or "0"

def isPrime(n):
    if n <= 1:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
        
    return True

def solution(n, k):
    final = number(n, k)
    
    final = list(final.split('0'))

    answer = 0
    for i in final:
        if i != '':
            if isPrime(int(i)):
                answer += 1
                
    return answer

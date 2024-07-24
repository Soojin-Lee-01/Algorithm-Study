from math import gcd
def get_gcd(arr):
    g = arr[0]
    # 배열을 돌면서 gcd를 구함 
    for i in range(1,len(arr)):
        g = gcd(arr[i],g)
    return g

def solution(arrayA, arrayB):
    answer = 0   
    a_gcd = get_gcd(arrayA)
    b_gcd = get_gcd(arrayB)
    
    for a in arrayA:
        if a % b_gcd == 0:
            break
    else:
        answer = max(b_gcd,answer)
        
    for b in arrayB:
        if b % a_gcd == 0:
            break
    else:
        answer = max(a_gcd,answer)
                    
    return answer

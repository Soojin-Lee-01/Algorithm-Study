def gcd(a, b): # 두 수의 최대공약수를 구함
    while b:
        a, b = b, a%b
    return a

def lcm(a, b): # 두 수의 최소공배수를 구함
    return a * b // gcd(a, b)

def solution(arr):
    lcm_value = arr[0]
    for num in arr[1:]:
        lcm_value = lcm(lcm_value, num) # 배열의 차례대로 최소공배수를 구함
    return lcm_value
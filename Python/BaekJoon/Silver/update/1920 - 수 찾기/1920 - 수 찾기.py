def binary_search(arr, target):
    left, right = 0, len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target: 
            return True
        elif arr[mid] < target:  
            left = mid + 1
        else: 
            right = mid - 1

    return False  

N = int(input())
data = list(map(int, input().split()))
data.sort() 

M = int(input())
answer = list(map(int, input().split()))

for target in answer:
    if binary_search(data, target):
        print(1)
    else:
        print(0)

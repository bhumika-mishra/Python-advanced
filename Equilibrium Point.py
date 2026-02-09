def equilibriumpoint(arr):
    leftsum = 0 
    rightsum = 0
    n = len(arr)

    for i in range(n):
        leftsum = 0 
        rightsum = 0 
        for j in range(i):
            leftsum += arr[j]
        for j in range(i+1,n):
            rightsum += arr[j]
        if leftsum == rightsum:
            return i 
    return -1
arr = [1,-3,9,0,3,2,2]   
print("Element:", arr[equilibriumpoint(arr)]) 

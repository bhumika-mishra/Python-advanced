def water(a,a_size):
    lefttallest = [0]*a_size
    righttallest = [0]*a_size
    water = 0 
    lefttallest[0] = a[0]
    for i in range(1,a_size):
        lefttallest[i] = max(lefttallest[i-1],a[i])
        righttallest[a_size-1] = a[a_size-1]
    for i in range(a_size-2,-1,-1):
         righttallest[i] = max(righttallest[i+1],a[i])
    for i in range(0,a_size):
        water += min(lefttallest[i],righttallest[i] - a[i])
        return water
b = [2,1,0,3,0,1,3,2,0,0,1]    
bars = len(b)
print("Water : ", water(b,bars))
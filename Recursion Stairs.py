def ways(stairs):
    if stairs<0:
        return 0
    if stairs == 0:
        return 1 
    twoS = 0
    oneS = 0
    if (stairs>=2):
        twoS = ways(stairs-2)
    oneS = ways(stairs-1)
    return twoS+oneS
stairs = int(input("Enter the no. of stairs : "))   
print("No. of ways to climb: ", ways(stairs)) 
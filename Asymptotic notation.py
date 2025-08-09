def Oconst(n):
    sum = 0 
    sum = n*(n+1)/2
    print(sum)

def On(n):
    sum = 0
    step = 0
    for i in range (n+1):
        sum = sum+i
        step = step+1
    print(sum)
    print("steps for On :", step)

def On2(n):
    sum = 0 
    step=0
    for i in range(n+1):
        for j in range(i):
            sum = sum+1
            step = step+1
    print(sum)        
    print("steps for On2 :", step)

n = int(input("Enter a no."))
Oconst(n)
On(n)
On2(n)
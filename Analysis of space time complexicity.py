def prints(n):
    if (n<=1):
        return
    print("Hi")
    prints(n/2)
    prints(n/2)    
n = int(input("Enter a no.")) 
prints(n)   

def sum(n):
    return n*(n+1)/2
def arraysum(a):
    sum = 0 
    for i in a:
        sum  = sum + i
    return (sum)     
a = [12,3,4,15]
print(arraysum(a))
print(sum(12))

def sum1(n):
    if (n<=0):
        return
    return n+sum(n-1)
print(sum1(5))
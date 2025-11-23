#Head Recursion
def headrec(n,num):
    if n>num:
        return
    headrec(n+1,num)
    print(n)
n= int(input("Enter n to print 1 to n : "))    
#headrec(1,n)

#Tail Recursion
def tailrec(n,num):
    if n>num:
        return
    print(n)
    tailrec(n+1,num)
n= int(input("Enter n to print 1 to n : "))    
#tailrec(1,n)

#Tree recursion
def incdec(n,num):
    if(n<1 or n>num):
        return
    print(n)
    incdec(n-1,num)
    print(n)
n= int(input("Enter n to print 1 to n : "))    
incdec(n,n)    

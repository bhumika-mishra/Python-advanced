#Head Recursion
def headrec(n,num):
    if n>num:
        return
    headrec(n+1,num)
    print(n)
n= int(input("Enter n to print 1 to n : "))    
headrec(1,n)
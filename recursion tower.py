def hanoi(n,a,b,c):
    if n==1:
        print("move disk 1 from rod",a,"to rod",b)
        return
    hanoi(n-1,a,c,b)
    print("move disk",n,"to rod",a,"to rod",b)
    hanoi(n-1,c,b,a)
n = 4
hanoi(n,'A','C','B')
    
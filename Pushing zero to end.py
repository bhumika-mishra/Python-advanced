def zero(a,a_size):
    zero1 = 0 
    nonzero = 0 
    while (nonzero != a_size):
        if a[nonzero] != 0:
            a[nonzero], a[zero1] = a[zero1], a[nonzero]
            zero1 += 1
        nonzero += 1
a = [23,0,56,0,34,0,7,23]    
a_size = len(a)
zero(a,a_size)
print("New Array : ",a)     
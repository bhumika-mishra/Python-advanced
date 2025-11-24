#sorted list
def checksorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])
a = [1,2,3,5,6,8,2]
if checksorted(a):
    print("\n Yes given array is sorted")
else:
     print("\n No given array is not sorted")

#sum using recursion
def arraytotalsum(a):
    length = len(a)
    if length == 1 :
        return a[0]
    return a[0] + arraytotalsum(a[1:])
a = [1,2,3,6]
print("Array total sum :",arraytotalsum(a))
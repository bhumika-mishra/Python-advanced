def factorial(n):
    if n<= 1 :
        return 1
    else:
        return n*factorial(n-1)
def sum(n):
    if n<=0:
        return 0
    else:
        return n+sum(n-1)
n = int(input("Enter a number : "))
print(f"Factorial of {n} is {factorial(n)}")   
print(f"Sum of {n} natural no. is {sum(n)}")      

number = int(input("Enter a no. : "))
add = 0 
while number>0:
    digit = number % 10
    add = add + digit
    number = number//10
print(add) 
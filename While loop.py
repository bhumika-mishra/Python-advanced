'''number = int(input("Enter a no. : "))
rev = 0 
while number>0:
    digit = number % 10
    rev = rev*10 + digit
    number = number//10
print(rev) '''   

'''number = int(input("Enter a no. : "))
count = 0 
while number>0:
    digit = number % 10
    count += 1
    number = number//10
print(count)    '''

running = True
sum = 0
while running :
    number = int(input("Enter a no. or press 0 to quit : "))
    sum = sum + number
    if number == 0 :
        running = False
print("Sum is :", sum)        
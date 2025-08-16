number = input("Enter a no.")
len = len(number)
number = int(number)
result = 0 
temp = number
while temp>0:
    digit = temp%10
    result = result + digit**len
    temp = temp//10
if result == number:
    print("The number is an Armstrong no.")
else:
    print("The number is not an Armstrong no.") 

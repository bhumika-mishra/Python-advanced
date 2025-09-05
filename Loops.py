list1 = [1,2,3,4,5,6,7,8,9,10]
odd = 0
for i in list1:
    if i%2 == 1:
        odd += 1
print(odd)     

name = input("Enter your name : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowelcount = 0
for i in name :
    if i in vowels:
        vowelcount += 1
print(vowelcount)


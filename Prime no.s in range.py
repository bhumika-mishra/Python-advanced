lower = int(input("Enter lower range :"))
higher = int(input("Enter higher range :"))

for j in range (lower,higher):
    prime = True
    for i in range (2,j):
     if j % i == 0:
        prime = False
        break
    if prime:
        print(f"The number {j} is a prime number")
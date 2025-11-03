primeNumbers=[]

for number in range(2,251):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            primeNumbers.append(number)

print("these are prime numbers between 1 and 250")
print(primeNumbers)

with open("Results.txt","w") as file:
    for p in primeNumbers:
        file.write(str(p) + ", ")

# prime_numbers.py
# Script to display and store all prime numbers between 1 and 250

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate primes between 1 and 250
primes = [str(num) for num in range(1, 251) if is_prime(num)]

# Display primes
print("Prime numbers between 1 and 250:")
print(", ".join(primes))

# Save results to file
with open("/home/scripted/Aws_reStart/Week_05_Python_Programming/results.txt", "w") as f:
    f.write("Prime numbers between 1 and 250:\n")
    f.write(", ".join(primes))

print("\nResults saved to results.txt")


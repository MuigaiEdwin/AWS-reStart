# Python Practice Exercises 🐍

A comprehensive collection of Python exercises from beginner to intermediate level.

## 📚 Table of Contents

1. [Basic Syntax & Data Types](#1-basic-syntax--data-types)
2. [Control Flow](#2-control-flow)
3. [Functions](#3-functions)
4. [Lists & Tuples](#4-lists--tuples)
5. [Dictionaries & Sets](#5-dictionaries--sets)
6. [String Manipulation](#6-string-manipulation)
7. [File Handling](#7-file-handling)
8. [Object-Oriented Programming](#8-object-oriented-programming)
9. [List Comprehensions & Generators](#9-list-comprehensions--generators)
10. [Error Handling](#10-error-handling)

---

## 1. Basic Syntax & Data Types

### Exercise 1.1: Variable Assignments
```python
# Create variables for your name, age, and height
# Print them in a formatted sentence

# Your code here:
```

**Solution:**
```python
name = "Alice"
age = 25
height = 5.6

print(f"My name is {name}, I'm {age} years old, and {height} feet tall.")
```

### Exercise 1.2: Type Conversion
```python
# Convert the string "123" to an integer
# Convert the integer 456 to a string
# Convert the string "3.14" to a float

# Your code here:
```

**Solution:**
```python
str_num = "123"
int_num = int(str_num)
print(int_num, type(int_num))

num = 456
str_num = str(num)
print(str_num, type(str_num))

float_str = "3.14"
float_num = float(float_str)
print(float_num, type(float_num))
```

### Exercise 1.3: Basic Operators
```python
# Calculate the area of a rectangle (length=10, width=5)
# Calculate the remainder when 17 is divided by 5
# Check if 15 is greater than 10 and less than 20

# Your code here:
```

**Solution:**
```python
area = 10 * 5
print(f"Area: {area}")

remainder = 17 % 5
print(f"Remainder: {remainder}")

result = 15 > 10 and 15 < 20
print(f"15 is between 10 and 20: {result}")
```

---

## 2. Control Flow

### Exercise 2.1: If-Else Statements
```python
# Write a program that checks if a number is positive, negative, or zero

# Your code here:
```

**Solution:**
```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### Exercise 2.2: For Loops
```python
# Print all even numbers from 1 to 20

# Your code here:
```

**Solution:**
```python
for i in range(2, 21, 2):
    print(i, end=" ")

# Alternative:
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
```

### Exercise 2.3: While Loops
```python
# Create a countdown from 10 to 1, then print "Blast off!"

# Your code here:
```

**Solution:**
```python
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
```

### Exercise 2.4: Nested Loops
```python
# Print a multiplication table (1-5) using nested loops

# Your code here:
```

**Solution:**
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()
```

---

## 3. Functions

### Exercise 3.1: Basic Function
```python
# Create a function that calculates the area of a circle
# Formula: π * r²

# Your code here:
```

**Solution:**
```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(5))
```

### Exercise 3.2: Function with Multiple Parameters
```python
# Create a function that takes two numbers and an operator (+, -, *, /)
# Return the result of the operation

# Your code here:
```

**Solution:**
```python
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

print(calculator(10, 5, '+'))
print(calculator(10, 5, '/'))
```

### Exercise 3.3: Function with Default Parameters
```python
# Create a greeting function with a default name parameter

# Your code here:
```

**Solution:**
```python
def greet(name="Guest", time="day"):
    return f"Good {time}, {name}!"

print(greet())
print(greet("Alice"))
print(greet("Bob", "morning"))
```

### Exercise 3.4: Return Multiple Values
```python
# Create a function that returns both quotient and remainder

# Your code here:
```

**Solution:**
```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"Quotient: {q}, Remainder: {r}")
```

---

## 4. Lists & Tuples

### Exercise 4.1: List Operations
```python
# Create a list of your 5 favorite fruits
# Add a new fruit, remove one, and sort the list

# Your code here:
```

**Solution:**
```python
fruits = ["apple", "banana", "orange", "mango", "grape"]
print("Original:", fruits)

fruits.append("kiwi")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.sort()
print("After sort:", fruits)
```

### Exercise 4.2: List Slicing
```python
# Create a list of numbers 1-10
# Get the first 3 numbers, last 3 numbers, and every other number

# Your code here:
```

**Solution:**
```python
numbers = list(range(1, 11))
print("Full list:", numbers)
print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Every other:", numbers[::2])
```

### Exercise 4.3: List Methods
```python
# Find the maximum, minimum, and sum of a list

# Your code here:
```

**Solution:**
```python
nums = [45, 23, 67, 12, 89, 34]
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Sum: {sum(nums)}")
print(f"Length: {len(nums)}")
print(f"Average: {sum(nums)/len(nums)}")
```

### Exercise 4.4: Tuples
```python
# Create a tuple with coordinates (x, y, z)
# Try to unpack it into separate variables

# Your code here:
```

**Solution:**
```python
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"X: {x}, Y: {y}, Z: {z}")

# Tuples are immutable
# coordinates[0] = 5  # This would raise an error
```

---

## 5. Dictionaries & Sets

### Exercise 5.1: Dictionary Basics
```python
# Create a dictionary for a student with name, age, and grades
# Add a new key, update a value, and delete a key

# Your code here:
```

**Solution:**
```python
student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 78]
}

student["email"] = "john@email.com"
print("After adding email:", student)

student["age"] = 21
print("After updating age:", student)

del student["grades"]
print("After deleting grades:", student)
```

### Exercise 5.2: Dictionary Methods
```python
# Create a dictionary and practice get(), keys(), values(), items()

# Your code here:
```

**Solution:**
```python
person = {"name": "Alice", "city": "NYC", "job": "Engineer"}

print(person.get("name"))
print(person.get("salary", "Not specified"))

print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

for key, value in person.items():
    print(f"{key}: {value}")
```

### Exercise 5.3: Sets
```python
# Create two sets and find union, intersection, and difference

# Your code here:
```

**Solution:**
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric difference:", set1 ^ set2)
```

---

## 6. String Manipulation

### Exercise 6.1: String Methods
```python
# Practice upper(), lower(), strip(), replace(), split()

# Your code here:
```

**Solution:**
```python
text = "  Hello World  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("World", "Python"))
print(text.split())

sentence = "Python,is,awesome"
print(sentence.split(','))
```

### Exercise 6.2: String Formatting
```python
# Format strings using f-strings, format(), and %

# Your code here:
```

**Solution:**
```python
name = "Alice"
age = 25
height = 5.6

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}, Height: {height:.1f}")

# format()
print("Name: {}, Age: {}, Height: {:.1f}".format(name, age, height))

# % operator
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))
```

### Exercise 6.3: String Operations
```python
# Check if a string is a palindrome

# Your code here:
```

**Solution:**
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
```

---

## 7. File Handling

### Exercise 7.1: Writing to Files
```python
# Write a list of names to a text file

# Your code here:
```

**Solution:**
```python
names = ["Alice", "Bob", "Charlie", "Diana"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names written to file!")
```

### Exercise 7.2: Reading from Files
```python
# Read and print contents of a file

# Your code here:
```

**Solution:**
```python
# Read entire file
with open("names.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Exercise 7.3: Append to Files
```python
# Append new data to an existing file

# Your code here:
```

**Solution:**
```python
with open("names.txt", "a") as file:
    file.write("Eve\n")
    file.write("Frank\n")

print("Names appended!")
```

---

## 8. Object-Oriented Programming

### Exercise 8.1: Basic Class
```python
# Create a Dog class with name, breed, and bark method

# Your code here:
```

**Solution:**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def info(self):
        return f"{self.name} is a {self.breed}"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())
print(my_dog.info())
```

### Exercise 8.2: Bank Account Class
```python
# Create a BankAccount class with deposit and withdraw methods

# Your code here:
```

**Solution:**
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"

account = BankAccount("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
```

### Exercise 8.3: Inheritance
```python
# Create a Vehicle parent class and Car child class

# Your code here:
```

**Solution:**
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def info(self):
        return f"{super().info()} with {self.doors} doors"

my_car = Car("Toyota", "Camry", 4)
print(my_car.info())
```

---

## 9. List Comprehensions & Generators

### Exercise 9.1: List Comprehension
```python
# Create a list of squares of numbers 1-10

# Your code here:
```

**Solution:**
```python
# Traditional way
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# List comprehension
squares = [i**2 for i in range(1, 11)]
print(squares)

# With condition
even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)
```

### Exercise 9.2: Dictionary Comprehension
```python
# Create a dictionary mapping numbers to their squares

# Your code here:
```

**Solution:**
```python
squares_dict = {i: i**2 for i in range(1, 6)}
print(squares_dict)

# Filter vowels from a string
text = "hello world"
vowels = {char: text.count(char) for char in text if char in 'aeiou'}
print(vowels)
```

### Exercise 9.3: Generator Expression
```python
# Create a generator for even numbers

# Your code here:
```

**Solution:**
```python
even_gen = (i for i in range(1, 11) if i % 2 == 0)
print(list(even_gen))

# Generator function
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print(list(fibonacci(10)))
```

---

## 10. Error Handling

### Exercise 10.1: Try-Except
```python
# Handle division by zero error

# Your code here:
```

**Solution:**
```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Invalid input type!"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))
```

### Exercise 10.2: Multiple Exceptions
```python
# Handle multiple exception types

# Your code here:
```

**Solution:**
```python
def process_input(value):
    try:
        num = int(value)
        result = 100 / num
        return result
    except ValueError:
        return "Please enter a valid number"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception as e:
        return f"An error occurred: {e}"

print(process_input("10"))
print(process_input("abc"))
print(process_input("0"))
```

### Exercise 10.3: Finally Block
```python
# Use try-except-finally for file handling

# Your code here:
```

**Solution:**
```python
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        return "File not found!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        if file:
            file.close()
            print("File closed")

# Better approach with context manager
def read_file_better(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"
```

---

## 🎯 Practice Projects

### Project 1: To-Do List Application
```python
# Create a command-line to-do list manager
# Features: add, view, complete, delete tasks
```

### Project 2: Number Guessing Game
```python
# Computer picks a random number
# User has to guess it with hints (higher/lower)
```

### Project 3: Contact Book
```python
# Store contacts with name, phone, email
# Add, search, update, delete contacts
```

### Project 4: Simple Calculator
```python
# Build a calculator with all basic operations
# Include error handling and history feature
```

### Project 5: Word Counter
```python
# Count words, characters, sentences in text
# Find most common words
```

---

## 📝 Tips for Practice

1. **Start Small**: Begin with basic exercises and gradually increase difficulty
2. **Debug Actively**: Use print() statements to understand code flow
3. **Read Error Messages**: They tell you exactly what went wrong
4. **Experiment**: Modify solutions and see what happens
5. **Build Projects**: Apply concepts to real-world problems
6. **Read Others' Code**: Learn different approaches on GitHub
7. **Practice Daily**: Consistency is key to improvement

## 🔗 Resources for Further Learning

- [Python Official Documentation](https://docs.python.org/3/)
- [LeetCode](https://leetcode.com/) - Coding challenges
- [HackerRank](https://www.hackerrank.com/) - Python exercises
- [Codewars](https://www.codewars.com/) - Kata challenges
- [Real Python](https://realpython.com/) - Tutorials and articles

---

Happy Coding! 🚀
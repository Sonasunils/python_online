# fn definition,fn call

# -----------------------------------------
# 1. Simple Function (No argument, No return)
# -----------------------------------------

def hello():
    print("Hello, Welcome to Python Functions")

hello()


# -----------------------------------------
# 2. Function with argument, No return
# -----------------------------------------

def greet(name):
    print("Hello", name)

greet("Sona")


# -----------------------------------------
# 3. Function with argument and return value
# -----------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# -----------------------------------------
# 4. Function without argument but with return
# -----------------------------------------

def get_number():
    return 100

num = get_number()
print("Returned number:", num)


# -----------------------------------------
# 5. Function to check Even or Odd
# -----------------------------------------

def check_even_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

check_even_odd(7)


# -----------------------------------------
# 6. Function to find square
# -----------------------------------------

def square(n):
    return n * n

print("Square:", square(5))


# -----------------------------------------
# 7. Function to find factorial
# -----------------------------------------

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))


# -----------------------------------------
# 8. Function to check Prime number
# -----------------------------------------

def check_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "is Prime")
    else:
        print(n, "is Not Prime")

check_prime(7)


# -----------------------------------------
# 9. Function to reverse a number
# -----------------------------------------

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

print("Reversed number:", reverse_number(1234))


# -----------------------------------------
# 10. Function using default argument
# -----------------------------------------

def country(name="India"):
    print("Country:", name)

country()
country("USA")


# -----------------------------------------
# 11. Function using keyword argument
# -----------------------------------------

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Anu")


# -----------------------------------------
# 12. Function to find maximum of two numbers
# -----------------------------------------

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", find_max(10, 25))

import math

def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = 5
print(f"Factorial of {num} (Iterative): {factorial_iterative(num)}")

def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
num = 5
print(f"Factorial of {num} (Recursive): {factorial_recursive(num)}")

num = 5
print(f"Factorial of {num} (math module): {math.factorial(num)}")
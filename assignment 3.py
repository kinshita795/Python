#Task 1: Calculate Factorial Using a Function 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")

#Task 2: Using the Math Module for Calculations
import math
num = float(input("Enter a number for calculations: "))
sqrt_value = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)
print(f"The square root of {num} is: {sqrt_value}")
print(f"The natural logarithm of {num} is: {natural_log}")
print(f"The sine of {num} is: {sine_value}")

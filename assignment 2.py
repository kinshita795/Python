#TASK1: check if the number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
#TASK2: Sum of Integers from 1 to 50 Using a Loop
total_sum = 0
for i in range(1, 51):
    total_sum = total_sum + i
print("The sum of integers from 1 to 50 is:", total_sum)
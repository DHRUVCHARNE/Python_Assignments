print("Hello, World!")
# Variables to store name, age, and hobby
name = "Dhruv"
age = 25
hobby = "coding"

# Print the variables
print("Name:", name)
print("Age:", age)
print("Hobby:", hobby)

# This line prints "Hello, World!" to the console
print("Hello, World!")

# Variables to store name, age, and hobby
name = "Dhruv"  # Stores the name
age = 25        # Stores the age
hobby = "coding"  # Stores the favorite hobby

# Print the variables
print("Name:", name)  # Prints the name
print("Age:", age)    # Prints the age
print("Hobby:", hobby)  # Prints the hobby
# Take an integer input from the user
num = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero and print the result
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# Take a year input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
# Print the first 10 natural numbers
for i in range(1, 11):
    print(i)
# Take an integer input from the user
num = int(input("Enter a number: "))

# Initialize a counter
i = 1

# Use a while loop to print the multiplication table
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
# Iterate through numbers 1 to 10
for i in range(1, 11):
    # Skip numbers divisible by 3
    if i % 3 == 0:
        continue
    print(i)
# Iterate through numbers 1 to 10
for i in range(1, 11):
    # Stop printing if the number is greater than 5
    if i > 5:
        break
    print(i)
# Define the greet function
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Dhruv")
# Define a function that returns the sum of two numbers
def add_numbers(a, b):
    return a + b

# Call the function and print the result
result = add_numbers(5, 3)
print("The sum is:", result)

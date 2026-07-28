# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
  total = 0
  for num in numbers:
    total += num
    return total

def calculate_sum9numbers):
  total = calculate_sum(numbers)
  count = 0
  for _  in numbers:
    count += 1
    return total / count

def calculate_max(numbers):
  maximum = numbers[0]
  for num in numbers:
    if num > maximum:
      maximum=num
return minimum

count = int(input("How many numbers?"))
num = [] 
for i in range(count):
  num=int(input(f"Enter number {i + 1}: "))

  if num <=0:
    print(Error: Only positive integers are allowed.")
    exit()
    numbers.append(num)

    print("\nResults:")
    print("Sum:", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:" calculate_max(numbers))
    print("Minimum:", calculate_min(numbers))
      

def fibonacci_for_loop(n):
    fib_sequence = [0, 1]  # Initialize the first two Fibonacci numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two numbers
        fib_sequence.append(next_number)
    return fib_sequence[:n]  # Return only the first 'n' numbers

# Generate and print the first 10 Fibonacci numbers
print("First 10 Fibonacci numbers (for loop):", fibonacci_for_loop(10))


def collect_numbers():
    numbers = []  # Initialize an empty list
    while True:
        user_input = input("Enter a number (type 'stop' to finish): ")
        if user_input.lower() == "stop":
            break  # Exit the loop if the user types 'stop'
        try:
            number = int(user_input)  # Convert input to an integer
            numbers.append(number)  # Add the number to the list
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input
    return numbers

# Collect numbers from the user
collected_numbers = collect_numbers()
print("Numbers entered:", collected_numbers)

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Generate the first 20 Fibonacci numbers using recursion
fib_sequence = [] 
for i in range(20):
    fib_number = fibonacci_recursive(i) 
    fib_sequence.append(fib_number) 

# Print the generated sequence
print("First 20 Fibonacci numbers (recursion):", fib_sequence)

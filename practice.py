multiply = lambda x, y: x * y
result = multiply(5, 3)  # Pass values 5 and 3
print(result)  # Output: 15
# Define a lambda function that calls a print statement
print_and_multiply = lambda x, y: (print(f"Multiplying {x} and {y}"), x * y)[1]

result = print_and_multiply(5, 3)  # Pass values 5 and 3
print(result)  # Output: 15

# Define a lambda function that returns a tuple with the result and a print statement
print
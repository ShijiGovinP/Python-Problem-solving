def generate_brackets(n):
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    result = '{' * n + '}' * n
    return result
value = 2
output = generate_brackets(value)
print(output)

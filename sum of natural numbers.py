n = int(input("Enter a natural number: "))
if n > 0:
    numbers = n * (n + 1) // 2
    print("The sum of the first", n, "natural numbers is:",numbers)
else:
    print("Please enter a positive number")

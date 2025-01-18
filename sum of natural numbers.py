n = int(input("Enter a natural number: "))
if n > 0:
    print(f"The sum of the first {n} natural numbers is: {n * (n + 1) // 2}")
else:
    print("Please enter a positive number.")

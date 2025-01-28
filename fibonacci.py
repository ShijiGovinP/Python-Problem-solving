def fibonacci_series(n):
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
        print(c, end=" ")

if __name__ == "__main__":
    fibonacci_series(int(input("Enter the number of terms: ")))

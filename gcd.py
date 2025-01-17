def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a% b)
a= 56
b = 98
result = gcd(a, b)
print(f"The GCD of {a} and {b} is {result}")

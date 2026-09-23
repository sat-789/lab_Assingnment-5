def fact(n):
    if n == 0:
        return 1
    else:
        s = n * fact(n - 1)
        return s


# Function call
n = int(input("Enter the number to calculate factorial: "))

print(f"Factorial of number {n} =", fact(n))
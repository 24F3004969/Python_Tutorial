def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return n


if __name__ == "__main__":
    print(factorial(5))

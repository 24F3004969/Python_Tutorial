def collatz(n):
    """
    A recursive function to compute the number of calls to the Collatz function of n

    Argument:
        n: integer
        Assume that 1 < n <= 32,000
    Returns:
        result: integer
    """
    return 0 if n == 1 else (1 + collatz(n / 2)) if n % 2 == 0 else (1 + collatz(3 * n + 1))


print(collatz(101))

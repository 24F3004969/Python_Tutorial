def steps(n):

    if n == 0:
        return 1
    elif n < 0:
        return 0

    return steps(n - 1) + steps(n - 2)


for i in range(-1,10):
    print(steps(i))
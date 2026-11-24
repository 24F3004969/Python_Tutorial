r = 30
for y in range(1, 2 * r):
    for x in range(1, 2 * r):
        k = x * x + y * y + r * r - 2 * r * (x + y)
        if k <= 0:
            print(" * ", end="")
        else:
            print("   ", end="")
    print()


R = 100
r = 0

while True:
    for y in range(1, 2 * R + 1):
        for x in range(1, 2 * R + 1):
            K = y * y + x * x + R * R - 2 * R * (x + y)
            L = y * y + x * x + r * r - 2 * r * (y + x)
            if K <= 0 and L >= 0:
                print("***", end="")
            else:
                print("   ", end="")
        print()
    print("\u001b[H")
    r = r + 1 if r <= 99 else 0


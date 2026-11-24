i = 7
while True:
    if (
        i % 2 == 1
        and i % 3 == 1
        and i % 4 == 1
        and i % 5 == 1
        and i % 6 == 1
        and i % 7 == 0
    ):
        print(i)
        break
    i = i + 1

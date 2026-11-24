def fibonacci_normal(n):
    a = 0
    b = 1
    print(a, ',', b, end='')
    for i in range(3, n):
        c = a + b
        print(',', c, end='')
        a = b
        b = c


def r_fibonacci(s, a, b, n) -> str:
    return r_fibonacci(s + ' ' + str((a + b)), b, a + b, n - 1) if n > 2 else s


def r_linear_search(l: list, index: int, num: int) -> int:
    return -1 if index == len(l) else index if l[index] == num else r_linear_search(l, index + 1, num)


def r_binary_search(l: list, start: int, end: int, num: int) -> int:
    return -1 if start > end else (start + end) // 2 if l[(start + end) // 2] == num else \
        r_binary_search(l, start, (start + end) // 2 - 1, num) \
            if l[(start + end) // 2] > num else r_binary_search(l, (start + end) // 2 + 1, end, num)

def bin_to_dec(bin):
    if len(bin) == 1:
        return int(bin)
    init = bin[:-1]
    last = bin[-1]
    return bin_to_dec(init) * 2 + int(last)



if __name__ == "__main__":
    fibonacci_normal(90)
    print()
    print(bin_to_dec('1011'))
    print(r_fibonacci('0 1', 0, 1, 150))
    print(r_linear_search([5, 7, 8, 912, 2, 3, -4, 56], 1, -4))
    print(r_binary_search([0, 1, 2, 3, 4, 5, 6, 17, 18, 29], 0, 9, 17))

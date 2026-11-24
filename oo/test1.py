def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
        L: list, type of elements could be anything
    Return:
        result: list
    """
    return rev(L, 0)


def rev(l: list, i: int) -> list:
    if i <= len(l) // 2:
        t = l[i]
        l[i] = l[len(l) - i - 1]
        l[len(l) - i - 1] = t
        return rev(l, i + 1)
    else:
        return l


print(reverse([1, 2, 3, 4, 5]))

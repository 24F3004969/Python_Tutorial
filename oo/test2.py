def linear(P, Q, k):
    if len(P) > 0:
        if Q[0] * k == P[0]:
            return linear(P[1:], Q[1:], k)
        else:
            return False
    else:
        return True


print(linear([ ], [], 2))

def myadd(a, b):

    if a > 0 and b > 0:
        return a + b

    if a < 0 and b < 0:
        return a + b

    if a == 0:
        return b

    if b == 0:
        return a

    if a > 0 and b < 0:
        if a > b:
            return a + b
        if a < b:
            return a + b

    return 0

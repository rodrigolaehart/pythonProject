def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

print(fatorial(5))
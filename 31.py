
def fz(n):
    if n % 15 == 0:
        return 3
    if n % 3 == 0:
        return 1
    if n % 5 == 0:
        return 2
    return 0

def sum_fz(n, m):
    return sum([fz(n + i) for i in range(m - n + 1)])
print(sum_fz(4, 11))

sum_fz = lambda n, m: sum(list(map(lambda i: 0 if i == 0 else 3 if i % 15 == 0 else 1 if i % 3 == 0 else 2 if i % 5 == 0 else 0, list(range(n, m + 1)))))
print(sum_fz(4,11))

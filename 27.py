# sum_int = lambda n, m: sum([n + i for i in range(m - n + 1)])

sum_int = lambda n, m: (lambda f: f(f, n, 0))(lambda f, n, total: f(f, n + 1, total + n) if n <= m else total)

# gcd = lambda *x: (lambda f: f(f, *x))(lambda f, x, y: f(f, y, x % y) if y else x)
print(sum_int(1, 3))


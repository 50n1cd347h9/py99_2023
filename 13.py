#f_to_f = lambda x, n: int(x * 10**(1 if n == 0 else n) + 0.5) / 10**(1 if n == 0 else n) if x >= 0 else int(x * 10**(1 if n == 0 else n) - 0.5) / 10**(1 if n == 0 else n)

f_to_f1 = lambda x: int(x * 10 + (0.5 if x >= 0 else -0.5)) / 10


print(f_to_f1(3.14159265))


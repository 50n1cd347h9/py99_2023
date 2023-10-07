#f_to_f = lambda x, n: int(x * 10**(1 if n == 0 else n) + 0.5) / 10**(1 if n == 0 else n) if x >= 0 else int(x * 10**(1 if n == 0 else n) - 0.5) / 10**(1 if n == 0 else n)

f_to_f = lambda x, n: int(x * 10**(1 if n == 0 else n) + (0.5 if x>= 0 else -0.5)) / 10**(1 if n == 0 else n) 

print(f_to_f(3.14159265, 2))


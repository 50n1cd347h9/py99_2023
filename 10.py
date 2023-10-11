from math import sqrt
eqn2 = lambda a, b, c: (lambda D: list(map(lambda x: (-b + x * (sqrt(D) if D >= 0 else sqrt(-1 * D) * 1j)) / (2 * a), [1, -1])))(b**2 - 4 * a * c)

eqn2 = lambda a, b, c: (lambda D: [(-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)] if D >= 0 else [(-b + sqrt(-1 * D) * 1j) / (2 * a), (-b - sqrt(-1 * D) * 1j) / (2 * a)])(b**2 - 4 * a * c)

# def eqn2(a, b, c):
#     ans = list(range(2))
#     
#     if (b**2 - 4 * a * c) >= 0:
#         ans[0] = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
#         ans[1] = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
#     else:
#         ans[0] = (-b + math.sqrt(-1 * (b**2 - 4 * a * c)) * 1j) / (2 * a)
#         ans[1] = (-b - math.sqrt(-1 * (b**2 - 4 * a * c)) * 1j) / (2 * a)
# 
#     return ans
    
print(eqn2(1, 2, 4))


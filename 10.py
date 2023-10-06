import math
eqn2 = lambda a, b, c: []
def eqn2(a, b, c):
    ans = list(range(2))
    
    if (b**2 - 4 * a * c) >= 0:
        ans[0] = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        ans[1] = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    else:
        ans[0] = (-b + math.sqrt(-1 * (b**2 - 4 * a * c)) * 1j) / (2 * a)
        ans[1] = (-b - math.sqrt(-1 * (b**2 - 4 * a * c)) * 1j) / (2 * a)

    return ans
    
print(eqn2(1, 2, 4))


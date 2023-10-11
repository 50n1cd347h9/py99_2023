sun_tzu = (lambda f: f(f, 0))(lambda f, i: i if ((i % 3 == 1) and (i % 5 == 2) and (i % 7 == 3)) else f(f, i + 1))

# def sun_tzu():
#     i = 0
# 
#     while True:
#         if (i % 3 == 1) and (i % 5 == 2) and (i % 7 == 3):
#             return i
#         i = i + 1



gcd = lambda *x: (lambda f: f(f, *x))(lambda f, x, y: f(f, y, x % y) if y else x)




print(gcd(24, 9))  # 最大公約数
print(sun_tzu)

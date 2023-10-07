days = lambda m1, d1, m2, d2: (lambda days: sum([days[i] for i in range(m2)]) - sum([days[i] for i in range(m1)]) - d1 + d2)([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30])

# def days(m1, d1, m2, d2):
#     days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
#     diff = sum([days[i] for i in range(m2)]) - sum([days[i] for i in range(m1)]) - d1 + d2 
#     return diff

print(days(12, 31, 1, 1))

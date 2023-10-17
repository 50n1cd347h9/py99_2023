median = lambda xs: (lambda val: xs[val - 1] if len(xs) % 2 != 0 else (xs[val - 1] + xs[val]) / 2)(int(len(xs) / 2 + 0.5))

print(median([1,2,3,4,5,6,7,8,9,10,11,12]))

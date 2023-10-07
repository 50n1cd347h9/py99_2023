era = lambda year: [(f"{x[0]}元年" if (year - x[1]) == 0 else f"{x[0]}{year - x[1] + 1}年") for x in [("令和", 2019), ("平成", 1989), ("昭和", 1926)] if year >= x[1]][0]

print(era(1984))

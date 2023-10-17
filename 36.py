mode = lambda xs: (lambda max_value, max_count:)(0, 0)

def mode(xs):
    max_value, max_count  = 0, 0
    for i in range(len(xs)) :
        count = 0

        for j in range(len(xs)):
            if xs[i] == xs[j]:
                count += 1

        if count > max_count:
            max_count = count
            max_value = xs[i]
    return max_value

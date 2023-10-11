sunlive_ = (lambda f: f(f, 0, 0))(lambda f, n, total: total if n < 0 else f(f, int(input()), total+n))


# def sunlive_():
#     nums = []
#     while True:
#        usr_input = int(input())
#        nums.append(usr_input)
# 
#        if usr_input < 0:
#            print(sum([x for x in nums])) 
#            break


print(sunlive_())

# reverse_str = lambda s: (lambda f: f(f, "", 0) )(lambda f, ret_val, i: f(f, ret_val + s[-(i + 1)], i + 1) if i < len(s) else ret_val)
reverse_str = lambda s: s[::-1]
# def reverse_str(s):
#     ret_val = ""
#     for i in range(len(s)):
#         ret_val += s[-(i + 1)]
#     return ret_val

print(reverse_str("aiueo"))

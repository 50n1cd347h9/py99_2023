time_to_int = lambda hh, mm, ss: hh * 3600 + mm * 60 + ss 
sec_between = lambda  h1, m1, s1, h2, m2, s2: time_to_int(h2, m2, s2) - time_to_int(h1, m1, s1)
print(sec_between(1,2,3,4,1,2) )

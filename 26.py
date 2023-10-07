from datetime import date as d

days_between = lambda y1, m1, d1, y2, m2, d2: (d(y2, m2, d2) - d(y1, m1, d1)).days


is_normal_triangle = lambda x, y, z: True if ((x**2 == y**2 + z**2) or (y**2 == z**2 + x**2) or (z**2 == x**2 + y**2)) else False
is_normal_triangle = lambda x, y, z: x**2 == y**2 + z**2 or y**2 == z**2 + x**2 or z**2 == x**2 + y**2


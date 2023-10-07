is_triangle = lambda x, y, z: False if ((x >= y + z) or (y >= z + x) or (z >= x + y)) else True

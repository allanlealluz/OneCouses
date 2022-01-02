import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    value = math.sqrt(sq)
    if value.is_integer():
        result = int(value) + 1
        result = result ** 2
        print(result)
        return result
    else:
        return -1
find_next_square(121)
find_next_square(625)
find_next_square(319225)
find_next_square(15241383936)
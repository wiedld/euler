
def triangle_num(threshold):
    """For a given threshold, responding to a num of divisors,
    what is the triangle number?"""

    # make triangle numbers
    # pattern:
    #     1 layer = 1 * 1     = 1
    #     2 layer = 2 * 1.5   = 3
    #     3 layer = 3 * 2     = 6
    layer = 1
    multiplier = 1.0

    while True:
        tri_num = layer * multiplier
        list_factors = find_factors(tri_num)

        if len(list_factors) >= threshold:
            return tri_num

        layer += 1
        multiplier += 0.5



def find_factors(N):
    factors = []
    start, end = 1, N

    # divide in half
    while start <= end:
        # make sure evenly divisible
        if N%start == 0:
            if start == end:
                factors.append(start)
            else:
                factors.extend([start, end])

        start = start + 1
        end = N / start

    return factors


print triangle_num(5)
print triangle_num(500)
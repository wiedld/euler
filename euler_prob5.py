# bigO:
    # n (list comprehension)
    # while loop
        # n (list comprehension), and sum.  == 2n
        # while loop breaks when answer found....increments in 20.  How do a bigO on this?


def smallest_evenly_div(high_divider):
    """finding the lowest number which is divided by everything up to high_divider.  If high_divider = 20, step up each increment by 20, since it has to be divisible by 20"""
    list_dividers = [x for x in range(1, high_divider+1)]
    print list_dividers

    num = high_divider    # lowest possible "high divider"
    while True:
        remainders = [num%x for x in list_dividers]
        if sum(remainders) == 0:
            break
        num+=high_divider   # step up increments of highest common denominator
    return num

print smallest_evenly_div(20)
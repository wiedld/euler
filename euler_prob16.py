
def sum_exp_nums(base, exp):
    product = 1.0

    while exp > 0:
        product = product * base

        exp = exp - 1

    result_str = str(int(product))

    # sum
    digit_sum = 0
    for str_digit in result_str:
        digit_sum = digit_sum + int(str_digit)

    return digit_sum


print sum_exp_nums(2, 1000)


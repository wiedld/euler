# big O:
    # 2 list comprehensions, and 2 sums.  Not nested.
    # 4n

def sum_of_squares(num):
    return sum([x**2 for x in range(1,num+1)])

def square_the_sum(num):
    return (sum([x for x in range(1,num+1)]))**2

def diff_sqsum_sumsq(num):
    return square_the_sum(num) - sum_of_squares(num)


print diff_sqsum_sumsq(10)
print diff_sqsum_sumsq(100)

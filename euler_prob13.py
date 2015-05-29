
def sum_large_nums(num_list):
    """
        take a list of large int, each int with the same # of digits,
        sum, and return only the first 10 digits
    """

    # starting value of e
    e = len(str(num_list[0])) - 10.0
    sum = 0.0

    for str_num in num_list:
        num = int(str_num)
        e_num = num/(10**e)
        sum += e_num

        # reset e if gets too large
        if len(str(int(sum))) > 10:
            sum = sum/10
            e += 1

    return int(sum)


alist = []
f = open("num_list.txt")
contents = f.read()
alist = contents.split("\n")

print sum_large_nums(alist)
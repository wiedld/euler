# BigO = worst case = n + n + sum(1/2 nums) = 2 1/2 n


def sum_even_fib_nums(n):
    return sum([x for x in get_fib_nums(n) if x%2==0])




def get_fib_nums(max_num):
    list_fibs = [1,2]

    while list_fibs[-1] < max_num:
        list_fibs.append(list_fibs[-2]+list_fibs[-1])

    list_fibs.pop(-1)
    return list_fibs




res = sum_even_fib_nums(90)
ans = 2+8+34

print res
print ans

euler = sum_even_fib_nums(4000000)
print euler

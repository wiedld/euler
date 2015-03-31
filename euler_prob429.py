## jumped a few pages ahead, out of curiosity.

## note - this only works for the base case.
# Not the test case, as it takes too long to run.
# lesson learned -- on the point of project euler and efficent code!!!

# going back to start at the beginning.  And learning time efficiency.


def sum_squares_unitary_divisors(n):
    """(1) a num n, calc n! = divider_of.  e.g. 4! = 24 divider divider_of."""
    """  (2) Then take divider_of and find out factors (24 can be divided by 1,2,3,4,6,7,9,12,24).  """
    """(3) get unitary divisor. take divider_of/x = y.  and see if x and y have any common dividers (other than 1).  e.g. x = 2. 24/2=12=y.  x(2) and y(12) are both dividible by 2.   e.g. x=8 24/8=3=y.  x(8) and y(3) are not divisible by anything above 1.  """
    """(4) square each unitary divisor.  and sum."""
    divisor_of = get_n_factorial(n)
    print "n! is:", divisor_of
    list_of_ud = get_unitary_divisors(divisor_of)
    print "unitary divisors are:", list_of_ud

    total = 0
    for ud in list_of_ud:
        total += (ud*ud)

    return total




def get_n_factorial(n):
    total = 1
    for num in range (1,n+1):
        total = total*num
    return total




def get_unitary_divisors(divisor_of):
    list_divisors_d = get_list_divisors(divisor_of) # list divisors of 24
    print "got list of divisors, line 31"

    list_unitary_divisors = []

    for num in list_divisors_d:                # num is x from doc string example
        print "started assessing num:", num
        possible_coprime = divisor_of/num        # y from doc string example
        factors_of_num = get_list_divisors(num)
        factors_of_coprime = get_list_divisors(possible_coprime)

        # figure out if any common factors
        unitary_divisor = True
        for i in factors_of_num:
            for j in factors_of_coprime:
                if (i==j) and (i>1):
                    unitary_divisor = False     # if any common factor, is not ud

        # if is a unitary divisor, then add to list:
        if unitary_divisor == True:
            list_unitary_divisors.append(num)

    return list_unitary_divisors




def get_list_divisors(d):
    list_divisors = []
    for num in range(1,d+1):
        if d%num == 0:
            list_divisors.append(num)
    return list_divisors


print sum_squares_unitary_divisors(4)   # answer should be 650

Sn = sum_squares_unitary_divisors(100000000)
print "Sn:", Sn
outcome = Sn%1000000009
print "outcome:", outcome


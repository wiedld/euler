# (1) find factors
    # don't add to factors if already divided by a factor
# (2) list_factors[-1]

# bigO ? nlogn + n*(nlogn)?
# first is the find_factors(n) which is nlogn.
# for loop is n, with nested call to find_factors (nlogn).


def largest_prime(n):
    list_factors = find_factors(n)
    # print list_factors

   # check if prime
    prime_factors = []

    for factor in list_factors:
        prime = True
        subfactors_list = find_factors(factor)
        # print subfactors_list
        if len(subfactors_list) > 0:
            prime = False
        if prime == True:
            prime_factors.append(factor)

    print prime_factors

    return prime_factors[-1]



def find_factors(n):
    # try the divide and conquer method
    start = 2
    end = n
    factors = []

    while start < end:
        if n%start == 0:
            factors.extend([start,end])
            end = n/start
            # print "new end:", end
        start +=1
    return factors



print "test 13195:"
print largest_prime(13195)
print "actual:"
print largest_prime(600851475143)

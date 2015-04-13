# (1) find factors
    # don't add to factors if already divided by a factor
# (2) list_factors[-1]


# worst case: n is a prime number.
    # find_factors for initial list of factors = O(n)
    # but then the for loop doesn't run because lust_factors is empty.
    # total = O(n)

# worst case: lots of list_factors.
    # find_factors for initial list of factors = nlogn?  or n?
    # the for loop is O(m) where m is the length of the list.
        # then has find_factors run on each. is nested mlogm or m?
        # considering len() as constant.
    # total = n + m*m = n + m^2




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

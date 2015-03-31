# bigO:
    # while loop (n)
    # but inside is the Sieve --> divide and conquer?
    # n * nlogn?


def find_primes_pos(position):
    list_primes = [2,3,5]
    num = 2
    while len(list_primes)<position:

        # faster computation.  Sieve of Eratosthenes
        if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:

            list_dividers = [x for x in range(1,num) if num%x==0]
            if len(list_dividers) == 1:
                list_primes.append(num)
        num+=1

    return list_primes[-1]



print find_primes_pos(6)
print find_primes_pos(10001)

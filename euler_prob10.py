
def sum_primes(N):
    num_list = [x for x in range(N)]
    # make 0 and 1 be false
    num_list[0], num_list[1] = 0,0

    for i in range(2, len(num_list)):

        # remove multiples of each prime, starting with #2
        multiple = 2
        while multiple * i < len(num_list):
            num_list[multiple*i] = 0
            multiple += 1

    return sum(num_list)


print sum_primes(10) # 17
print sum_primes(2000)  # 277050
print sum_primes(2000000)  # 142913828922



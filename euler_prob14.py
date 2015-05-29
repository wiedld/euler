
def is_even(N):
    return N/2


def is_odd(N):
    return (3*N)+1


def longest_collatz(ceiling):

    max_length = 0
    num_with_max = None

    for i in range(1, ceiling+1): # don't start at 0
        curr = i
        seq_length = 1

        while curr != 1:

            if curr%2 == 0:
                curr = is_even(curr)
            else:
                curr = is_odd(curr)

            seq_length += 1

        if seq_length > max_length:
            max_length = seq_length
            num_with_max = i

    return num_with_max


print longest_collatz(1000000)
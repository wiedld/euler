# big O:
# nested for loops, but second for loop is partial list.
# nested inside is a reverse function.
# n^3?  yet is fast because use a num_floor?


def max_palindrome(num_ceiling, num_floor):
    max_palin = 0
    multiplier = []

    for x in range(num_ceiling,num_floor,-1):
        multiplier.append(x)
        for y in multiplier:
            possible = x*y
            rev_possible= reverse_num(possible)
            if rev_possible == possible:
                # first palin found
                if max_palin == 0:
                    max_palin = possible
                # getting the max palin
                else:
                    max_palin = max(max_palin, possible)
    return max_palin


def reverse_num(num):
    rev_num = ""
    # using the base ten method
    while num:
        digit = num%10
        rev_num = rev_num + str(digit)
        num = int(num/10)
    # print rev_num
    return int(rev_num)


print max_palindrome(99,50)
print max_palindrome(999,900)  #906609

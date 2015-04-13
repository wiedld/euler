
def karatsuba_multiply(x,y):

    # evidently, you keep the recursive calls on the same level for each multiplication.  Only divide and conquer (recursive) for both, or for neither.
    x_str, y_str = str(x), str(y)
    if len(x_str) <= 2 or len(y_str) <= 2:
        return x * y
    max_len = max(len(x_str), len(y_str))
    midpt = max_len/2

    # instead of string slicing, base 10 on original num
        # this resolves problem if two nums are very uneven in length.
    # a = int(x_str[:-midpt])
    # b = int(x_str[-midpt:])
    # c = int(y_str[:-midpt])
    # d = int(y_str[-midpt:])
    a = x/(10**midpt)
    b = x%(10**midpt)
    c = y/(10**midpt)
    d = y%(10**midpt)
    # print "a: %d, b: %d, c: %d, d: %d" % (a,b,c,d)

    z0_hi = karatsuba_multiply(a,c)
    # print "z0:", z0_hi

    z1 = karatsuba_multiply( (a+b), (c+d) )
    # print "z1:", z1

    z2_low = karatsuba_multiply(b,d)
    # print "z2:", z2_low

    e = midpt * 2
    sub_tot1 = z0_hi*(10**e)
    sub_tot2 = (z1-(z0_hi+z2_low))*10**(e/2)
    sub_tot3 = z2_low

    # print "sub_tot1:",sub_tot1
    # print "sub_tot2:",sub_tot2
    # print "sub_tot3:",sub_tot3

    return sub_tot1 + sub_tot2 + sub_tot3



# works = uneven digits
num1 = 567830649089
num2 = 123
print "test:", num1 * num2
print karatsuba_multiply(num1, num2)

# works = 4 digits
num3 = 5678
num4 = 1234
print "test:", num3 * num4
print karatsuba_multiply(num3, num4)

# works = 5 digits
num5 = 56789
num6 = 12345
print "test:", num5 * num6
print karatsuba_multiply(num5, num6)

# works = 6 digits
num7 = 567823
num8 = 123456
print "test:", num7 * num8
print karatsuba_multiply(num7, num8)



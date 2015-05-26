import math


def pythagorean_triplet(target_sum):
    # a2 + b2 = c2
    # in all cases (stifel, ozaman), a+b > c.
    max_c = target_sum/2

    while True:
        for c in range(max_c,1,-1):

            max_a = c-1
            for a in range(max_a,1, -1):

                b = math.sqrt((c*c) - (a*a))
                if (a + b + c) == target_sum:
                    print "a:", a
                    print "b:", b
                    print "c:", c
                    return (a*b*c)






print 5*12*13
print pythagorean_triplet((5+12+13)) #780

print pythagorean_triplet(1000)

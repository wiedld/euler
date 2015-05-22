


# re-done in list comprehension
print (sum([x for x in range(3,1000,3) if x % 15 != 0]) +
      sum([x for x in range(5,1000,5)]))


# BigO = no best/worst case = with n being max(1000)
#  n/3 + n/5 = n

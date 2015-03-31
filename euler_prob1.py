
# def find_sum_multiples_3_5(n):
#     """under <n, get all 3,5 multiples. sum"""
#     total = 0
#     for num in range(1,n):
#         if (num%5 == 0) or (num%3 == 0):
#             total = total + num
#     return total

# print (find_sum_multiples_3_5(10) == 23)
# print (find_sum_multiples_3_5(20) == 78)
# print (find_sum_multiples_3_5(30) == 195)

# print find_sum_multiples_3_5(1000)


# re-done in list comprehension
print (sum([x for x in range(3,1000,3) if x % 15 != 0]) +
      sum([x for x in range(5,1000,5)]))


# BigO = worst case = 2n + summing = 3n
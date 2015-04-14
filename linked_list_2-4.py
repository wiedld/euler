# PROBLEM
# You have two numbers represented by a linked list, where each node contains a sin- gle digit The digits are stored in reverse order, such that the 1’s digit is at the head of the list Write a function that adds the two numbers and returns the sum as a linked list
# EXAMPLE
# Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
# Output: 8 -> 0 -> 8


def LL_sum(LL1, LL2):
    LL1_N = LL1.head
    LL2_N = LL2.head
    LL3 = LL()
    LL3_N = LL3.head

    while True:
        if LL1_N==None and LL2==None:
            return LL3      # note this LL3 has a final node which is empty.  If needed, could trim with helper.

        summed = node_data(LL1_N) + node_data(LL2_N)
        LL3_N.data = summed%10 + LL3_N.data
        LL1_N, LL2_N = node_next(LL1_N), node_next(LL2_N)

        LL3_N = output_LL_next(LL3_N, summed/10)



def node_data(N):
    if N==None:
        return 0
    else:
        return N.data

def node_next(N):
    if N==None:
        return None
    else:
        return N.next

def output_LL_next(N, data):
    N.next = LL_N(data)
    return N.next

class LL_N(Object):
    def __init__(self, data=None):
        self.data = data

class LL(Object):
    def __init__(self, head=LL_N(),tail=LL_N()):
        self.head = head
        self.tail = tail


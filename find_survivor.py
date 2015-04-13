def find_survivor(n):
    seats = []

    for seat in range(1,n+1):
        seats.append(seat)

    count = 0
    while len(seats) > 1:

        if count == len(seats):
            count = 0
        if count > len(seats):
            count = 1

        seats.pop(count)
        count +=1

    return seats[0]


print find_survivor(10)
print find_survivor(100)

#######################################################
#######################################################

class Seat(object):
    data = None
    next = None

    def __init__(self, seat_num, next):
        self.data = seat_num
        self.next = next

    def __repr__(self):
        return "<Seat number: %d>" % (self.data)



def survivor_with_linked_list(n):
    #create seats linked to each other
        # make last seat, and link in reverse
    #append to list
    seats = []
    curr_seat = Seat(n,None)    # last seat. not yet linked
    seats.append(curr_seat)

    for num in range(1,n):  # for num 1 to 100, for seats 99 down to 1.
        # making seats in reverse.  seat num is n-num
        new_seat = Seat(n-num, curr_seat)
        seats.append(new_seat)
        curr_seat = new_seat

    # reverse the list, so seats are in order
    seats = seats[::-1]

    # link the last seat to the first
    seats[-1].next = seats[0]


    curr_seat = seats[-1]
    while curr_seat != curr_seat.next:
        skipped_ahead_seat = curr_seat.next.next
        curr_seat.next = skipped_ahead_seat
        curr_seat = skipped_ahead_seat

    return curr_seat.data


print survivor_with_linked_list(10)
print survivor_with_linked_list(100)



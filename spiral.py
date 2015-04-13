
n = 4

def spiral(n):
    output = [(0,0)]
    last = output[-1]       # (0,0)
    for x in range(1,n):
        next = (last[0]+x, last[1])  #(1,0) then (2,0)
        output.append(next)

    while n>1:
        last = output[-1]
        for y in range(1,n):
            next = (last[0], last[1]+y)     #(2,1) then (2,2)
            output.append(next)
        last = output[-1]
        for x in range(1,n):
            next = (last[0]-x, last[1])      #(1,2) then (0,2)
            output.append(next)
        n = n-1

        last = output[-1]
        for y in range(1,n):
            next = (last[0], last[1]-y)     #(0,1)
            output.append(next)
        last = output[-1]
        for x in range(1,n):
            next = (last[0]+x, last[1])
            output.append(next)
        n = n-1

    return output





print spiral(n)
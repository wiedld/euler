# APPROACH:
# - model the grid as the coordinate points
# - a 2x2 grid has 3x3 points (corners)
# - find paths through matrix
#
# subproblems:
# - make "NxN matrix" where the value is the location
#     - really just counting up i and j until both equals N
# - traverse by either i +1 or j +1, but not both
#
# - time efficiency is a problem with large N.
# - solution: Pascal's triangle.
#       - count paths to diagonals
#       - occurances^2 (mirror image)


def count_paths(N):

    diagonals = paths_to_diagonal(N)
    counts = count_occurances(diagonals)

    # pascal.  sum (occurance^2)
    total = 0
    for k,v in counts.items():
        total = total + (v**2)

    return total


def paths_to_diagonal(N, i=0, j=0, moves=0, diagonals=[]):
    # base cases
    if moves == N:
        diagonals.append([i,j])
        return diagonals

    # update state
    moves += 1

    # left path
    paths_to_diagonal(N, i+1, j, moves, diagonals)
    # right path
    paths_to_diagonal(N, i, j+1, moves, diagonals)

    return diagonals


def count_occurances(alist):
    counts = {}
    # count occurances to diagonal
    for item in alist:
        k = str(item)
        if k in counts:
            counts[k] += 1
        else:
            counts[k] = 1

    return counts


print count_paths(20)

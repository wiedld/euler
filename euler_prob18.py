import math

def max_path_pyramid(pyr_list, path_subtotal=0, i=0, j=0, max_path=0):
    """recursive down the tree.  Finding all poss paths to leaves.  Take max."""
    # base case
    if i == len(pyr_list):
        max_path = max(path_subtotal, max_path)
        return max_path

    path_subtotal = path_subtotal + int(pyr_list[i][j])
    i +=1

    # left child
    l_max = max_path_pyramid(pyr_list, path_subtotal, i, j, max_path)
    # right child
    r_max = max_path_pyramid(pyr_list, path_subtotal, i, j+1, max_path)

    return max(l_max, r_max)


def path_to_pyramid_list(path):
    f = open(path)
    contents = f.read()

    list_lines = contents.split("\n")
    for i in range(len(list_lines)):
        line = list_lines[i]
        new_line = line.split(" ")
        list_lines[i] = new_line

    return list_lines


print max_path_pyramid(path_to_pyramid_list("num_pyramid.txt"))


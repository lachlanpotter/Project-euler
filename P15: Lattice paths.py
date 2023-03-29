#=========================================================================
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
#=========================================================================

#IDEA: recursion using the method of counting these paths I happen to know. In which one starts at the top left labelled 1, labelling each vertex with the sum of the incoming labels. This method will generalise to a directed graph.

N = 20

#dictionary to speed up the paths function
dict = {(0,0):1}

def paths(n,m):
    '''paths takes in two non-negative ints and calculates the number of monotonic paths from the top left to the bottom right vertex of a graph consisting of an nxm array or cubes'''
    if n < 0 or m < 0:
        return 0
    while (n,m) not in dict:
        dict[(n,m)] = paths(n-1,m) + paths(n,m-1)
    return dict[(n,m)]

print('the number of paths through a', N, "by", N, "grid is", paths(N,N))
'''
 Write a function that returns the intersection of two arrays. The intersec-
 tion is a third array that contains all values contained within the first two
 arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8]
 is [2, 4] .
 Your function should have a complexity of O(N). (If your programming
 language has a built-in way of doing this, don’t use it. The idea is to build
 the algorithm yourself.)

 O(N + M)
'''
def intersection_of_two_arrays(A, B):
    l1 = set(A)
    return [x for x in B if x in l1]

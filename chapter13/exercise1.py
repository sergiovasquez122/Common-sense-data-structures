'''
1. Given an array of positive numbers, write a function that returns the
greatest product of any three numbers. The approach of using three
nested loops would clock in at O(N 3 ), which is very slow. Use sorting to
implement the function in a way that it computes at O(N log N) speed.
(There are even faster implementations, but we’re focusing on using
sorting as a technique to make code faster.)
'''
def greatest_product_of_three(a):
    b = a[:]
    b.sort()
    n = len(b)
    return max(a[n - 1] * a[n - 2] * a[n - 3], a[n - 1] * a[0] * a[1])

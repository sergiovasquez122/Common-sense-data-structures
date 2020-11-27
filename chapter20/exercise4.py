'''
4. You're writing a function that accepts an array of numbers and computes the
highest product of any two numbers in the array. At first glance, this is easy,
as we can just find the two greatest numbers and multiply them. However, our
array can contain negative numbers and look like this:

    [5, -10, -6, 9, 4]

In this cae, it's actually the product of the two largest numbers, -10 and -6
that yield the highest product of 60.

We could use nested loops to multiply every possible pair of numbers, but this
would take O(N**2). Your job is to optimize the function so that it's a speedy
O(N)

solution is O(N)
'''
def find_highest_product_of_two(A):
    first_largest = -float('inf')
    second_largest = -float('inf')
    first_smallest = float('inf')
    second_smallest = float('inf')
    for x in A:
        if first_largest < x:
            second_largest = first_largest
            first_largest = x
        elif first_largest > x and second_largest < x:
            second_largest = x

        if first_smallest > x:
            second_smallest = first_smallest
            first_smallest = x
        elif first_smallest < x and second_smallest > x:
            second_smallest = x

    return max(first_largest * second_largest, first_smallest * second_smallest)

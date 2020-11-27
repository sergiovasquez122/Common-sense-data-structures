'''
6. You're writing a function that accepts an array of unsorted integers and
return sth lenght of the longest consecutive sequence among them. The sequence
is formed by integers that increase by 1. For example, in the array:

    [10, 5, 12, 3, 55, 30, 4, 11, 2]

the longest consecutive sequence is 2-3-4-5. These four integers form an
increasing sequence because each integer is on greater than the previous one.
While there's also a sequence of 10-11-12, it's only a sequence of three
integers. In thise case, the funtion should return 4, since that's the length
of the longest consecutive sequence that can be formed from this array.

If we sorted the array, we can then traverse the array just once to find the
longest consecutive sequence. However, the sorting itself would take O(N *
LOG(N)). Your job is to optimize the function so that it takes O(N) time.
'''
def longest_consecutive_sequence(A):
    l = {key : True for key in A}
    removed_element = 0
    result = 1
    while removed_element != len(l):
        for x in l:
            if l[x]:
                sequence = 1
                l[x] = False
                removed_element += 1
                temp = x - 1
                while temp in l:
                    sequence += 1
                    removed_element += 1
                    l[temp] = False
                    temp -= 1
                temp = x + 1
                while temp in l:
                    sequence += 1
                    removed_element += 1
                    l[temp] = False
                    temp += 1
                result = max(sequence, result)
    return result

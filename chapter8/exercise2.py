'''
write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is ["a", "b", "c", "d",
"c", "e",
"f"] , the function should return "c" , since it’s duplicated within the array.
(You can assume that there’s one pair of duplicates within the array.)
Make sure the function has an efficiency of O(N).
'''
def first_duplicate_found(A):
    l1 = set()
    for x in A:
        if x in l1:
            return x
        l1 = l1 | x
    return None

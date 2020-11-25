'''
 Write a function that accepts a string that contains all the letters of the
 alphabet except one and returns the missing letter. For example, the string,
 "the quick brown box jumps over a lazy dog" contains all the letters of the
 alphabet
 except the letter, "f" . The function should have a time complexity of O(N).
'''
def find_missing_letter(A):
    marked = [False for _ in range(27)]
    for x in A:
        marked[ord(x) - 97] = True

    for idx, x in enumerate(marked):
        if x == False:
            return chr(idx + 97)
    return None

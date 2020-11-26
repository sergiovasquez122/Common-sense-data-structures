'''
2. Use recursion to write a function that accepts an array of numbers and
returns a new array containing just the even numbers.
'''
def even_numbers_only(l,result=[],idx=0):
    if idx >= len(l): 
        return result
    if l[idx] % 2 == 0:
        result.append(l[idx])
    return even_numbers_only(l, result, idx + 1)

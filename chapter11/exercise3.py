'''
3. There is a numerical sequence known as “Triangular Numbers.” The
pattern begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth
number in the pattern, which is N plus the previous number. For example,
the 7th number in the sequence is 28, since it’s 7 (which is N) plus 21
(the previous number in the sequence). Write a function that accepts accepts a
number for N and returns the correct number from the series'''
def triangular_number(n):
    if n == 1: return 1
    return n + triangular_number(n - 1)

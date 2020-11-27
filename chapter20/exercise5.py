from collections import deque
from math import log, floor
'''
5. You're creating software that analyzes
the data of body temperature readings taken
from hundres of human patients. These readings
are taken from healty people and range from 97.0
degrees Fahrenheit to 99.0 degrees Fahrenheit.
An importan point: within this application, the
decimal point never goes beyond the tenths place.

You are to write a function that sorts these
readings from lowest to highest.

This solution is O(N)
'''
def sort_temperature(A):
    B = A[:]
    for i in range(len(B)):
        B[i] *= 10
        B[i] = int(B[i])
    k = max(B)
    qs = [deque() for _ in range(11)]
    iteration = int(floor(log(k))) + 1
    current_power = 1
    while iteration != 0:
        for x in B:
            number = x // current_power
            digit = number % 10
            qs[digit].append(x)
        current_power *= 10
        counter = 0
        iteration -= 1
        for q in qs:
            while len(q) != 0:
                B[counter] = q.popleft()
                counter += 1
    return [x / 10 for x in B][::-1]


'''
3. implementations of a function that finds the greatest
number within an array. Write one function that is O(N2), one that is O(Nlog N), and one that is O(N).
'''
def brute_force(l):
    for i in range(len(l)):
        isTheGreatest = True

        for j in range(len(l)):
            if l[j] > l[i]:
                isTheGreatest = False
        if isTheGreatest:
            return l[i]
    return None

def better(l):
    b = l[:]
    return b[len(b) - 1]

def best(l):
    return max(l)

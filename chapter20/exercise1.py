# O(N + M)
def players_in_both_sports(A, B):
    a_set = set()
    for x in A:
        first_name = x[0]
        last_name = x[1]
        full_name = first_name + " " + last_name
        a_set.add(full_name)

    b_set = set()
    for x in B:
        first_name = x[0]
        last_name = x[1]
        full_name = first_name + " " + last_name
        b_set.add(full_name)
    return a_set.intersection(b_set)

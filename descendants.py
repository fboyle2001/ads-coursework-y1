digit_factorial = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
known = {}

def calculate_child(i):
    child = 0

    while i != 0:
        digit = i % 10
        child += digit_factorial[digit]
        i = i // 10
        
    return child

def find_strength(i, seen):
    if i in known:
        return known[i]

    if i in seen:
        last_seen_index = seen.index(i)
        loop_length = len(seen) - last_seen_index

        for x in seen[last_seen_index:]:
            known[x] = loop_length

        return 0

    seen.append(i)
    strength = 1 + find_strength(calculate_child(i), seen)
    
    if i not in known:
        known[i] = strength
        
    return strength

def find_strength_start(i):
    if calculate_child(i) == i:
        known[i] = 1
    
    return find_strength(calculate_child(i), [])

def descendants(a, b, k):
    count = 0
    
    for i in range(a, b):
        strength = find_strength_start(i)
        if strength == k:
            count += 1
            
    return count

def q2test():
    assert descendants(1,2,1) == 1
    print("passed a")
    assert descendants(1,200,1) == 6
    print("passed b")
    assert descendants(1,2000,3) == 33
    print("passed c")
    assert descendants(4000,6000,3) == 36
    print("passed d")
    assert descendants(123456,654321,20) == 4015
    print("passed e")
    assert descendants(1,1000000,59) == 402
    print("passed f")
    assert descendants(1,1000000,60) == 0
    print("passed g")

from eulerlib import time_algorithm

def time_test():
    time_algorithm(q2test)
    

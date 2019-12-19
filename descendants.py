digit_factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
known = {}
stored = {}

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
    
    if i not in known.keys():
        known[i] = strength
        
    return strength

def find_strength_start(i):
    if i in stored:
        return stored[i]
    
    start_child = calculate_child(i)
    length = find_strength(start_child, [])
    
    return length

def descendants(a, b, k):
    count = 0
    
    for i in range(a, b):
        strength = find_strength_start(i)
        stored[i] = strength
        
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
    time_algorithm(q2test, trials=1)
    

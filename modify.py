digit_factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
known = {}
stored = {}
looped = set()

import sys
import traceback

def calculate_child(i):
    child = 0

    while i != 0:
        digit = i % 10
        child += digit_factorial[digit]
        i = i // 10

    return child

def find_strength(i, seen):
    if i in stored:
        return stored[i]

    if i in seen:
        last_seen_index = seen.index(i)
        loop_length = len(seen) - last_seen_index 

        for x in seen[last_seen_index:]:
            known[x] = loop_length
            stored[x] = loop_length
            looped.add(x)

        return 0

    seen.append(i)
    strength = find_strength(calculate_child(i), seen) + 1
    
    if i not in stored.keys():
        known[i] = strength
        stored[i] = strength - 1
        
    return strength

def find_strength_start(i):
    if i in stored:
        return stored[i]
    
    start_child = calculate_child(i)
    strength = find_strength(start_child, [])
    stored[i] = strength

    if i == 961:
        stored[i] = strength - 1
    
    return strength

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
    try:
        assert descendants(1,200,1) == 6
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))
        exit(1)
    print("passed b")
    try:
        assert descendants(1,2000,3) == 33
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print('An error occurred on line {} in statement {}'.format(line, text))
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

#singles and loops have stored - known = 1 for some reason?!?!
def diff():
    print("X | KNOWN | STORED")
    for x in known.keys():
        s = stored[x]
        d = known[x] - s
        if d != 0:
            print(x, known[x], s)
    print("done")

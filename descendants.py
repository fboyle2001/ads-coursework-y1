digit_factorial = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
known = {}

def calculate_child(i):
    child = 0
    
    while i != 0:
        digit = i % 10
        child += digit_factorial[digit]
        i = i // 10
        
    return child

def find_descendants(i):
    #store a set of descendants to this point
    #then subtract the set of descendants after this point
    #will give total descendants of a number?
    seen = set()

    while i not in seen:
        seen.add(i)
        i = calculate_child(i)

    return len(seen)

def find_des_length(i, seen):
    if i in seen:
        #we are done but lets find the loop so we can memorise
        last_seen_index = seen.index(i)
        loop_length = len(seen) - last_seen_index
        
        for x in seen[last_seen_index:]:
            known[x] = loop_length

        for index, x in enumerate(seen[:last_seen_index]):
            known[x] = len(seen) - index - 1
            
        return known[seen[0]]
    else:
        seen.append(i)
        return find_des_length(calculate_child(i), seen)

f = lambda k: find_des_length(k, [])

def descendants(a, b, k):
    c = 0
    for i in range(a, b):
        l = find_des_length(i, [])
        #print(i, l)
        if l == k:
            c += 1
    return c 

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
    

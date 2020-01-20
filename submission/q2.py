#39 lines of code
digit_factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
known = {}
stored = {}

#Calculates the child of a number
def calculate_child(i):
    child = 0

    #Gets the right-most digit and then finds its digit factorial
    #Then takes mod 10 to remove the last digit and shift all of the
    #other digits left
    while i != 0:
        digit = i % 10
        child += digit_factorial[digit]
        i = i // 10

    return child

#Calculates the strength recursively by maintaining a temporary array
#to track which numbers have already been included
#I used an array over a set here as it allows calculation of the length
#of the loops as sets do not respect insertion order
def find_strength(i, seen):
    if i in known:
        return known[i]

    if i in seen:
        last_seen_index = seen.index(i)
        loop_length = len(seen) - last_seen_index

        #If we find a loop then store the length of each of these loops
        #since they appear in almost all sequences
        for x in seen[last_seen_index:]:
            known[x] = loop_length

        return 0

    seen.append(i)
    strength = find_strength(calculate_child(i), seen) + 1

    #Instead of waiting until we reach a number in the cycle
    #we can precompute it using the work already done in this cycle
    if i not in known.keys():
        known[i] = strength
        stored[i] = strength - 1
        
    return strength

#Initial setup before we actually do the recursion
def find_strength_start(i):
    if i in stored:
        return stored[i]
    
    start_child = calculate_child(i)
    strength = find_strength(start_child, [])
    stored[i] = strength
    
    return strength

def descendants(a, b, k):
    count = 0

    #Loops over the range and finds the strength of each number
    #Simply just maintains a count of the amount that = k
    for i in range(a, b):
        strength = find_strength_start(i)
        
        if strength == k:
            count += 1
            
    return count

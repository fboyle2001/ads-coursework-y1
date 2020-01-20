def hash_double(keys):
    table = ["-"] * 23

    for k in keys:
        #calculate the initial hash value
        hash_value = (4 * k + 7) % 23

        #if there is no collision then just put it in the table
        if table[hash_value] == "-":
            table[hash_value] = k
            continue

        initial_hash = hash_value
        double_hash = 17 - (k % 17)
        j = 0
        skip = False

        #iteratively test the double hash
        #if after 23 attempts we have not found a spot then we will loop
        #back around so there are no available spaces
        while table[hash_value] != "-":
            j += 1
            hash_value = (initial_hash + j * double_hash) % 23

            if j > 23:
                skip = True
                break

        if not skip:
            table[hash_value] = k

    return table

def hash_quartic(keys):
    table = ["-"] * 23

    #iteratively test the keys and calculate their hash value
    for k in keys:
        hash_value = (4 * k + 7) % 23
        initial_hash = hash_value
        j = 0
        skip = False

        #if the initial slot is free then the loop will not be entered
        #instead the value will be put in the correct spot immediately
        while table[hash_value] != "-":
            j += 1
            hash_value = (initial_hash + j ** 4) % 23

            #we can be certain we've gone full circle and this number
            #cannot be put in the hash table using this hash function
            #since (23 + A)^4 = A^4 = p (mod 23) for any A and some p.
            if j > 23:
                skip = True
                break

        if not skip:
            table[hash_value] = k

    return table

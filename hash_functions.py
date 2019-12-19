#need to think a bit more about this
# j ** 4 % 23 will not cover all remainders so we may get too many
#clashes and cant find a spot for the number
#[-1.75, -1.5, -1.25, -1.0, -0.75, -0.25, 0.25, 0.5, 1.25, 1.5, 2.25, 2.75, -19]
#this array will break it
def hash_quartic(keys):
    table = ["-"] * 23

    for k in keys:
        hash_value = int((4 * k + 7) % 23)
        initial_hash = hash_value
        j = 0
        skip = False

        while table[hash_value] != "-":
            j += 1
            hash_value = (initial_hash + j ** 4) % 23

            #we can be certain we've gone full circle and this number
            #cannot be put in the hash table using this hash function
            if j == 23:
                skip = True
                break

        if not skip:
            table[hash_value] = k

    #print(table)
    return table

def hash_double(keys):
    pass
    
def test_hq():
    assert hash_quartic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == [4, 10, 16, 22, 5, 11, 17, 23, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21]
    assert hash_quartic([19,38,57,76,95,114,133,152,171,190]) == ['-', 171, '-', 114, '-', 57, '-', '-', 190, '-', 133, '-', 76, '-', 19, '-', '-', 152, '-', 95, '-', 38, '-']
    assert hash_quartic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [71, 53, 59, 73, 5, 11, 17, 23, 29, 79, 41, 47, 7, 13, 19, 2, 31, 37, 43, 3, '-', 61, 67]
    print ("all tests passed")

def test_dh():
    assert hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == [4, 10, 16, 22, 5, 11, 17, 23, 6, 12, 18, 1, 7, 13, 19, 2, 8, 14, 20, 3, 9, 15, 21]
    assert hash_double([19,38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323,342,361]) == ['-', 171, 361, 114, 304, 57, 247, '-', 190, '-', 133, 323, 76, 266, 19, 209, '-', 152, 342, 95, 285, 38, 228]
    assert hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [67, 73, 79, 53, 5, 11, 17, 23, 29, '-', 41, 47, 7, 13, 19, 2, 31, 37, 43, 3, 71, 61, 59]
    print ("all tests passed")

def pattern():
    for j in range(0, 25):
        print(j, (j ** 4) % 23)

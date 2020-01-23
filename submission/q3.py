def LP(string):
    longest = [LOP(string)]
    n = len(string)

    #an even palindrome must have the centre 2 characters equal to each other
    #leave out the last character otherwise we will get an index error
    for centre in range(0, n - 1):
        left_pointer = centre
        right_pointer = centre + 1
        moves = 0

        #move along in blocks of 2 until we find identical characters
        #once we do try and expand the palindrome until we can't anymore
        #we know if we are correct because the two characters on each end
        #must be identical to each other
        while string[left_pointer] == string[right_pointer]:
            #print(string[left_pointer:right_pointer+1])
            moves += 1
            #we've hit the end of the string and so can't continue
            if left_pointer == 0 or right_pointer == n - 1:
                break

            left_pointer -= 1
            right_pointer += 1

        #the number of times we expanded * 2 = length of palindrome
        longest.append(moves * 2)
        
    return max(longest)

def LP2(string):
    n = len(string)
    longest = []
    #we want to consider all wrap arounds of the string
    for start_point in range(0, n):
        #once we have a wrap around version just call LP on it
        #store the longest palindrome
        wrap = string[start_point:n] + string[0:start_point]
        longest.append(LP(wrap))

    #get the longest palindrome from the list
    return max(longest)

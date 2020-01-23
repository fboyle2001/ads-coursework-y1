#q3test.py
#algorithms and data structures assignment 2019-20 q3
#matthew johnson 13 november 2019

#####################################################


def LOP(string):
    """finds the longest odd length palindrome within a given string"""
    
    def reflection(pivot, point):
        """given position of two characters pivot and point in a string, finds 
        the position of a character as far from pivot as point in the opposite 
        direction; i.e the position reached if point is reflected in pivot"""
        return 2 * pivot - point
    
    #find the length of the input string
    n = len(string)
    
    #create a list to record the longest odd length palindrome centred at each 
    #character; to initialise: the longest palindrome centred at string[0] 
    #has length 1
    longest = [1]
    
    #we need always to remember the palindrome found that extends farthest to 
    #the right by recording the position of its centre, leftmost and rightmost 
    #characters (of course, there is redundancy here)
    #we call this palindrome FARTHEST_RIGHT_PALINDROME
    #initially this is the one character palindrome at string[0]
    centre_FARTHEST_RIGHT_PALINDROME = 0
    right_FARTHEST_RIGHT_PALINDROME = 0
    left_FARTHEST_RIGHT_PALINDROME = 0
    
    #create a pointer to range over each of the other characters in string
    #each time through the for loop we seek to find the longest palindrome 
    #centred at string[pointer] and store this in the list longest
    for pointer in range(1,n): 
        
        #want initially to use the current entries in longest and what we 
        #know about FARTHEST_RIGHT_PALINDROME to find a long (but maybe not 
        #the longest) palindrome centred at pointer; 
        #then we will record the position of the right and leftmost characters 
        #of this palinderome using further pointers (left_pointer and 
        #right_pointer)
        #we also record its size in longest[pointer] which we might update later
        
        #if pointer is beyond right_FARTHEST_RIGHT_PALINDROME we have no useful 
        #information and know of only the single character palindrome at 
        #string[pointer]
        if pointer > right_FARTHEST_RIGHT_PALINDROME:
            right_pointer = pointer        
            left_pointer = pointer
            longest += [1]
        
        else:
            #if pointer is not beyond right_FARTHEST_RIGHT_PALINDROME then 
            #string[pointer] is a character within FARTHEST_RIGHT_PALINDROME
            #consider the character to left of centre_FARTHEST_RIGHT_PALINDROME 
            #at the same distance from the centre as pointer
            pointer_reflection = reflection(centre_FARTHEST_RIGHT_PALINDROME, pointer)
            
            #clearly a palindrome centred at pointer_reflection that lies 
            #completely within FARTHEST_RIGHT_PALPALINDROME has a mirror image 
            #centred at pointer; first recall the size of longest palindrome 
            #centred at pointer_reflection, which we call PALINDROME_LEFT
            PALINDROME_LEFT_size = longest[pointer_reflection] 
            
            #in fact, we are only interested in the subpalindrome of 
            #PALINDROME_LEFT inside FARTHEST_RIGHT_PALINDROME since, again, 
            #we know there is an identical palindrome also inside 
            #FARTHEST_RIGHT_PALINDROME centred at pointer; 
            #we call this SUBPALINDROME_LEFT and note that its leftmost 
            #character is either the leftmost character of PALINDROME_LEFT 
            #(if the whole of PALINDROME_LEFT is within 
            #FARTHEST_RIGHT_PALINDROME), or the leftmost character of 
            #FARTHEST_RIGHT_PALINDROME, whichever of these is farthest to the right
            left_SUBPALINDROME_LEFT = max(left_FARTHEST_RIGHT_PALINDROME, 
                                          pointer_reflection - PALINDROME_LEFT_size + 1)
            
            #now considering the reflection of SUBPALINDROME_LEFT around 
            #centre_FARTHEST_RIGHT_PALINDROME, we have a palindrome centred at 
            #pointer; its rightmost character is the reflection of the 
            #leftmost character of SUBPALINDROME_LEFT
            right_pointer = reflection(centre_FARTHEST_RIGHT_PALINDROME, left_SUBPALINDROME_LEFT)
            #and now we can find leftmost character in this palindrome 
            #centred at pointer
            left_pointer = reflection(pointer, right_pointer)
            #and record the length of the palindrome 
            longest += [(right_pointer - pointer) * 2 + 1]
            
        #if right_pointer now points to the left of right_FARTHEST_RIGHT_PAL 
        #we know the longest palindrome centred at pointer has been found and 
        #does not extend beyond right_FARTHEST_RIGHT_PALINDROME (because we 
        #know PALINDROME_LEFT is contained entirely within 
        #FARTHEST_RIGHT_PALINDROME) if right_pointer is at or beyond 
        #right_FARTHEST_RIGHT_PALINDROME  we see if the longest palindrome 
        #we have found can be extended
        if right_pointer >= right_FARTHEST_RIGHT_PALINDROME:
            
            #when we are done the palindrome centred at pointer will now be the 
            #palindrome that we have seen that extends farthest to the right
            centre_FARTHEST_RIGHT_PALINDROME = pointer
            right_FARTHEST_RIGHT_PALINDROME = right_pointer
            left_FARTHEST_RIGHT_PALINDROME = left_pointer
            
            #try to extend
            while True:
                #check that pointers can be moved without leaving the string
                if left_pointer == 0 or right_pointer == n-1:
                    break
                #move pointers
                left_pointer -= 1
                right_pointer += 1
                
                #see if longer palindrome has been found
                if string[left_pointer] == string[right_pointer]:
                    longest[pointer] += 2
                    right_FARTHEST_RIGHT_PALINDROME += 1
                    left_FARTHEST_RIGHT_PALINDROME -= 1
                else: 
                    break
    
    #return largest value found            
    return max(longest)
    
        
        
    
    
    
def tests():
    assert LOP("a") == 1
    assert LOP("abba") == 1
    assert LOP("abbac") == 1
    assert LOP("abcdefg") == 1
    assert LOP("abbabba") == 7
    assert LOP("banana") == 5
    
    assert LP("a") == 1
    assert LP("abba") == 4
    assert LP("abbac") == 4
    assert LP("abcdefg") == 1
    assert LP("abbabba") == 7
    assert LP("banana") == 5
    assert LP("abcdefgfhijkl") == 3
        
    assert LP2("a") == 1
    assert LP2("cbc") == 3
    assert LP2("abba") == 4
    assert LP2("abbac") == 5
    assert LP2("abcdefg") == 1
    assert LP2("abbabba") == 7
    assert LP2("banana") == 5
    assert LP2("abcdefgfhijkl") == 3
    
    
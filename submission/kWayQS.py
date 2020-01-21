import sys

def read_input(filename):
    A = []
    
    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A

def insertionsort(A):
    for pos, x in enumerate(A):
        lower = pos - 1

        while lower >= 0 and A[lower] > x:
            A[lower + 1] = A[lower]
            lower -= 1

        A[lower + 1] = x

    return A
   
def partition(A, k):
    #get k pivots
    pivots = A[len(A)-k:len(A)]
    #sort the pivots
    pivots = insertionsort(pivots)
    
    pivot_indexs = []
    partitioned = []

    #partition all elements below the lowest pivot
    for element in A:
        if element < pivots[0]:
            partitioned.append(element)

    #partition into groups between each pivot
    for i in range(0, k - 1):
        left = pivots[i]
        right = pivots[i + 1]

        partitioned.append(left)
        left_index = len(partitioned) - 1
        pivot_indexs.append(left_index)

        for element in A:
            if element > left and element < right:
                partitioned.append(element)

    #put the final pivot into its position
    partitioned.append(pivots[k - 1])
    right_index = len(partitioned) - 1
    pivot_indexs.append(right_index)

    #partition everything greater than the final pivot
    for element in A:
        if element > pivots[k - 1]:
            partitioned.append(element)
    
    return partitioned, pivot_indexs

def quicksort(A, k):
    if len(A) <= 2 * k:
        return insertionsort(A)

    partitioned, pivots = partition(A, k)

    #need to recurse to B[:pivots[0]-1]
    #then B[pivots[i] + 1:pivots[i + 1]]
    #then B[pivots[k - 1]+1:]

    sorted_array = quicksort(partitioned[:pivots[0]], k)

    #sort the partition and put the pivots into there correct place
    #in the final array
    for i in range(0, k - 1):
        left = pivots[i]
        sorted_array.append(partitioned[left])
        right = pivots[i + 1]
        sorted_array += quicksort(partitioned[left + 1:right], k)

    #put the final pivot into its correct spot and sort the final partition
    sorted_array.append(partitioned[pivots[k - 1]])
    sorted_array += quicksort(partitioned[pivots[k - 1] + 1:], k)
    return sorted_array

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A,k))
    
if __name__ == "__main__":
    main()

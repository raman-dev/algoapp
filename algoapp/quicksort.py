import random

SWAP = 100
LI_MOVE = 0
RI_MOVE = 1
P_MOVE = 2

def quicksort(string):
    #given an array of ints use quicksort algorithm to 
    #to sort the array
    #in place
    #nlogn complexity
    array = [int(char) for char in string]
    print(array)
    length = len(array)
    #random pivot
    #although better pivot selection is median of left mid right
    
    #now what move elements less than pivot to the left of pivot_index?
    #or pivot
    #i think we keep pivot index the same but move values greater 
    #than the pindex left and right of it
    #this is a recursive algorithm so 
    left_iter = 0
    right_iter = length - 1
    action_list = []#
    qs(left_iter,right_iter,length // 2,array,action_list)
    print(array)
    return action_list

#fully functioning quicksort
def qs(left_iter,right_iter,pivot_index,array,action_list):
    #now what?
    #move the pivot to the location its supposed to be
    partition_start = left_iter
    partition_end = right_iter
    pivot = array[pivot_index]
    #print("partition_start => "+str(partition_start))
    #print("partition_end => "+str(partition_end))
    #print("pivot_index => "+str(pivot_index))
    action_list.append({'NEW_PARTITION' :[left_iter,right_iter]})
    action_list.append({'P_MOVE':pivot_index})
    action_list.append({'LI_MOVE':left_iter})
    action_list.append({'RI_MOVE':right_iter})

    while left_iter < right_iter:
        #we can advance the left iter so long as it is
        #less than the pivot
        #we are moving over values that are less than the pivot
        #until we find a value that is greater than the pivot
        #so we don't have to swap values less than the pivot
        while left_iter <= partition_end and array[left_iter] <= pivot:
            left_iter += 1
            action_list.append({'LI_MOVE' : left_iter})

        #now what?
        if left_iter <= partition_end and left_iter < pivot_index :
            t = array[left_iter]
            array[left_iter] = pivot
            array[pivot_index] = t
            action_list.append({'SWAP':[pivot_index,left_iter]})
            action_list.append({'P_MOVE':left_iter})
            pivot_index = left_iter
            #print(array)
        while right_iter >= partition_start and array[right_iter] >= pivot:
            right_iter -= 1
            action_list.append({'RI_MOVE' : right_iter})
        if right_iter >= partition_start and right_iter > pivot_index :
            t = array[right_iter]
            array[right_iter] = pivot
            array[pivot_index] = t
            action_list.append({'SWAP': [pivot_index,right_iter]})
            action_list.append({'P_MOVE':right_iter})
            #since pivot moved to the location we found a value less than  or equal to pivot
            pivot_index = right_iter
            #print(array)
    
    #now the pivot is at the correct sorted location
    #so the remaining partitions are left of the pivot index and right of the pivot index
    

    if pivot_index - partition_start > 1:
        qs(partition_start,pivot_index - 1, (((pivot_index - 1) - partition_start) // 2) + partition_start,array,action_list)
    if partition_end - pivot_index > 1:
        qs(pivot_index + 1,partition_end,((partition_end - pivot_index) // 2) + pivot_index + 1,array,action_list)


"""for i in list(range(0,100)):
    array = [ random.randint(0,20) for val in range(0,20)]
    array_original = array.copy()
    for v in array_original:
        if v not in array:
            print("failed!")
            break"""
def heapify(arr, indx):
    # Max Heap. IF the sign (>) in the comparison is changed it becomes min heap
    # After swapping if the child node is greater then we see the chnaged item below it if it right,
    # if not then we call the function from there.

    left = indx*2
    right = indx*2 +1
    l = len(arr)

    # Finds the maximum which child is maximum
    if (left < l and arr[left]>arr[indx]):
        largest = left

    else:
        largest = indx

    if (right < l and arr[right]>arr[largest]):
        largest = right



    if (largest!=indx):
        arr[largest], arr[indx] = arr[indx], arr[largest]
        heapify(arr, largest)

    #print(arr)



array = [0,1,4,3,7,8,9,10]


# We loop from the level above the leaf nodes to the head
for i in range(int((len(array)-1)/2), 0, -1):
    heapify(array,i)

print(array)
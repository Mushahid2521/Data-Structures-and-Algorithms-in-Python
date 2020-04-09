def peakElement(arr, n):
    if n==1:
        return 0
    if n==2:
        return 0 if arr[0]>arr[1] else 1

    left = 0
    right = n-1

    while right>=left:
        if arr[left] > arr[left+1]:
            return left

        elif arr[right] > arr[right-1]:
            return right

        left+=1
        right-=1


print(peakElement([1, 3, 5, 4, 7, 10, 6], 7))

# Here 10 or 5 is the answer. Local Maximum is which is greater than its neighbour





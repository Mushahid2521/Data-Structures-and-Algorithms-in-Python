def firstDuplicate(array):
    l = len(array)

    for i in range(l):
        if array[abs(array[i])-1] < 0:
            return abs(array[i])

        # Make the found value index negative
        array[abs(array[i])-1] = -array[abs(array[i])-1]


print(firstDuplicate([2,1,1]))
# [2, -1, 1]
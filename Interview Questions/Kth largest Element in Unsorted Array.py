
# [3,2,1,5,6,4]
def kthlargest(array, kth):
    cur_max = -float("inf")

    for val in array:
        if val>cur_max:
            cur_max = val
            kth-=1

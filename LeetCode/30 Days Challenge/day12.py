def solve(array):
    """
    Sum of -1 and 1 makes it easy.
    Value with each sum is taken as Key
    first key is incerted at index
    Then again when its sum value comes then calculates the difference with present index
    """
    max_length = 0
    table = {0:0}
    cnt = 0
    for index, val in enumerate(array, 1):
        if val==0:
           cnt-=1

        else:
            cnt+=1

        if cnt in table:
            max_length = max(max_length, index-table[cnt])

        else:
            table[cnt] = index

    return max_length

print(solve([0,1,0,1,0,1]))

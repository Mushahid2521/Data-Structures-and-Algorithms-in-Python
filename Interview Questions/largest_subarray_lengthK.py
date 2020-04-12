def solve(array, k):
    l = len(array)
    sum = 0
    for i in range(k):
        sum+=array[i]

    left = 0
    new_sum = sum

    for i in range(1, l-k+1):
        new_sum = new_sum-array[i-1]+array[k+i-1]
        if new_sum > sum:
            left = i
            sum = new_sum


    return array[left:k+left]




print(solve([1,3,-1,-3,5,3,6,7], 3))
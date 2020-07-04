def findLongestSubarrayBySum(s, a):
    sumdict = {0:0}

    sum = 0
    left = 0
    right = -1

    for i in range(len(a)):
        sum += a[i]

        if sum-s in sumdict:
            if i-sumdict[sum-s] >= right-left:
                right = i
                left = sumdict[sum-s]

        if sum not in sumdict:
            sumdict[sum] = i+1

    if right!=-1:
        return [left+1, right+1]

    return [-1]



print(findLongestSubarrayBySum(3, [3]))
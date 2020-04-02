def maxSubArraySum(nums):
    l = len(nums)
    local_max, global_max = -float("inf"), - float("inf")
    for i in range(l):
        local_max = max(local_max + nums[i], nums[i])
        global_max = max(local_max, global_max)

    return global_max


def largestSum(array):
    l = len(array)
    cache = [None] * (l)

    def dp(i):
        if(i>=l):
            return 0

        if cache[i]!=None:
            return cache[i]

        cache[i] = max(array[i]+dp(i+1), array[i])

        return cache[i]

    dp(0)

    return max(cache)


array = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArraySum(array))
print(largestSum(array))

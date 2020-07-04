def sumInRange(nums, queries):
    cumulative_sum = [0] * len(nums)
    cumulative_sum[0] = nums[0]
    for i in range(1, len(nums)):
        cumulative_sum[i] += (cumulative_sum[i - 1] + nums[i])

    sum = 0
    for query in queries:
        sum += (cumulative_sum[query[1]] - cumulative_sum[query[0]] + nums[query[0]])

    return int(sum%(10e7+7))

print(sumInRange([-1000], [[0, 0]]))
def subsetIterative(nums):
    # Iterative
    rst = [[]]
    for num in nums:
        parent_len = len(rst)
        for i in range(parent_len):
            rst.append(rst[i] + [num])
    return rst

def subsetRecursive(nums):
    rst = []
    def helper(start, cur):
        rst.append(cur)
        for i in range(start, len(nums)):
            helper(i+1, cur+[nums[i]])

    helper(0, [])
    return rst


print(subsetIterative([1,2,3]))
print(subsetRecursive([1,2,3]))
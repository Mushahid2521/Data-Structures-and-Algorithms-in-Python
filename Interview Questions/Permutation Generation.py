
def permutation(nums):
    ans = []
    def perm(nums, start):
        if start==len(nums)-1:
            ans.append(nums)
            return

        for j in range(start, len(nums)):
            nums[j], nums[start] = nums[start], nums[j]
            perm(nums[:], start+1)

    perm(nums, 0)
    return ans


print(permutation([1,2,3]))



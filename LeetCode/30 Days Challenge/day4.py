def solve(array):
    l = len(array)
    left_idx = 0
    right_idx = l-1

    for idx, val in enumerate(array):
        if val==0:
            array[right_idx] = 0
            right_idx-=1

        else:
            array[left_idx] = val
            left_idx+=1

    print(array)


def solve2(array):
    l = len(array)
    if l==1:
        return

    left = 0
    right = 1

    while right<l:
        if array[left] == 0 and array[right]:
            array[left], array[right] = array[right], array[left]
            left+=1
            right+=1

        else:
            if array[left]==0:
                right+=1

            else:
                left+=1
                right+=1

    print(array)



class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return solve2(nums)


s = Solution()
print(s.moveZeroes([1,0]))

# class Solution:
#     def moveZeroes(self, nums) -> None:
#         n = len(nums)
#         if n > 1:
#             l, r = 0, 1
#             while r < n:
#                 if nums[l] == 0 and nums[r]:
#                     nums[r], nums[l] = nums[l], nums[r]
#                     l += 1
#                     r += 1
#                 else:
#                     if nums[l]:
#                         l += 1
#                     r += 1

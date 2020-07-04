# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        res = [0] * l
        left_prod = [0] * l
        left_prod[0] = 1

        right_prod = [0] * l
        right_prod[l - 1] = 1

        for i in range(1, l):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]

        for i in range(l - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]

        for i in range(l):
            res[i] = left_prod[i] * right_prod[i]

        return res
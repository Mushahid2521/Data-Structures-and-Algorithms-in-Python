# def findMedianSortedArrays(nums1, nums2):
#     nums = nums1 + nums2
#     nums = sorted(nums)
#
#     n = len(nums)
#     if n % 2 == 0:
#         left_idx = int(n / 2 - 1)
#         right_idx = left_idx + 1
#         median = (nums[left_idx] + nums[right_idx]) / 2
#
#     else:
#         idx = int(n / 2)
#         median = nums[idx]
#
#     return median
#
# print(findMedianSortedArrays([1,2], [3,4]))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        l = len(nums)

        if l % 2 == 0:
            left_idx = int(l / 2 - 1)
            right_idx = left_idx + 1
            median = (nums[left_idx] + nums[right_idx]) / 2

        else:
            idx = int(l / 2)
            median = nums[idx]

        return median

s = Solution()
print(s.findMedianSortedArrays([1,2], [3,4]))

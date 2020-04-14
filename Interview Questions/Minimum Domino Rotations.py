# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


class Solution:
    def minDominoRotations(self, A, B) -> int:
        a_cnt = [0] * 7
        b_cnt = [0] * 7

        l = len(A)
        for i in range(l):
            a_cnt[A[i]] += 1
            b_cnt[B[i]] += 1


        max_a = 0
        max_val_a = -float("inf")

        max_b = 0
        max_val_b = -float("inf")
        for i in range(7):
            if a_cnt[i] > max_val_a:
                max_val_a = a_cnt[i]
                max_a = i

            if b_cnt[i] > max_val_b:
                max_val_b = b_cnt[i]
                max_b = i


        if max_val_b >= max_val_a:
            res = l - max_val_b
            array1 = B
            array2 = A
            idx = max_b

        else:
            res = l - max_val_a
            array1 = A
            array2 = B
            idx = max_a

        #print(res, idx, A)
        for i in range(l):
            if array1[i]!=idx and array2[i]!=idx:
                return -1


        return res


s = Solution()
print(s.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))



class Solution:
    def kClosest(self, points, K):
        array = []
        for point in points:
            array.append(point[0] ** 2 + point[1] ** 2)

        idxs = [i[0] for i in sorted(enumerate(array), key=lambda x: x[1])]

        res = []
        for i in range(K):
            res.append(points[idxs[i]])

        return res


s = Solution()
print(s.kClosest([[1,3],[-2,2]], K = 1))
import heapq
# [3,2,1,5,6,4]
def kthlargest(array, kth):
    heapq.heapify(array)
    for _ in range(len(array)-kth+1):
        val = heapq.heappop(array)

    return val


print(kthlargest([3,2,1,5,6,4], 3))


import heapq

def kthSmallestInMatrix(matrix, kth):
    """
    Return the Kth smallest element in a sorted list

    1. One element in smaller than the left and below element.
    2. Use heap to store the present smaller elements at the top

    Complexity: O(klog(k))
    """
    if not matrix and kth<1:
        return

    row_len = len(matrix)
    col_len = len(matrix[0])

    s = set()
    s.add((0,0))
    heap = [(matrix[0][0], 0, 0)]

    while kth>1:
        top = heapq.heappop(heap)
        row, col = top[1], top[2]

        if row+1 < row_len and (row+1, col) not in s:
            heapq.heappush(heap, [matrix[row+1][col], row+1, col])
            s.add((row+1, col))

        if col+1 < col_len and (row, col+1) not in s:
            heapq.heappush(heap, [matrix[row][col+1], row, col+1])
            s.add((row, col+1))

        kth-=1

    return heap[0][0]

print(kthSmallestInMatrix([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8))



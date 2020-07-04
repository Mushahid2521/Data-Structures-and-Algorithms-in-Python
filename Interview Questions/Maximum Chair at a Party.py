"""
arr[]  = {1, 2, 10, 5, 5}
dep[]  = {4, 5, 12, 9, 12}

Below are all events sorted by time.  Note that in sorting, if two
events have same time, then arrival is preferred over exit.
 Time     Event Type         Total Number of Guests Present
------------------------------------------------------------
   1        Arrival                  1
   2        Arrival                  2
   4        Exit                     1
   5        Arrival                  2
   5        Arrival                  3    // Max Guests
   5        Exit                     2
   9        Exit                     1
   10       Arrival                  2
   12       Exit                     1
   12       Exit                     0
"""


def maximumChairs(arrival, leave):
    arrival.sort()
    leave.sort()

    l = len(arrival)
    chairs_now = 1
    max_chairs = 1
    time_of_mx_chairs = arrival[0]
    # First One take as arrival
    i = 1
    j = 0

    while i<l and j<l:
        # If the arrival is less then add arrival
        if arrival[i] <= leave[j]:
            chairs_now+=1
            if chairs_now > max_chairs:
                max_chairs = chairs_now
                time_of_mx_chairs = arrival[i]

            i+=1

        # Leave time is less
        else:
            chairs_now-=1
            j+=1

    return max_chairs, time_of_mx_chairs


print(*maximumChairs([1, 2, 10, 5, 5], [4, 5, 12, 9, 12]))

# import heapq
#
#
# class Solution:
#     def __init__(self):
#         pass
#
#     def minChairs(self, S, E):
#
#         # Form interval pairs (start time, end time)
#         intervals = [[S[i], E[i]] for i in range(len(S))]
#
#         # Sort intervals based on start time
#         intervals.sort(key=lambda x: x[0])
#
#         heap = []
#         res = 0
#
#         for interval in intervals:
#             if not heap or heap[0] > interval[0]:
#                 # If no chair is free allocate new chair
#                 res += 1
#                 heapq.heappush(heap, interval[1])
#             else:
#                 # If any chair is free
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, interval[1])
#
#         return res
#
#
# s = Solution()
# print(s.minChairs([1, 2, 10, 5, 5], [4, 5, 12, 9, 12]))


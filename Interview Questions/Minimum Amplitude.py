def solve(array):
    """
    Change at most 3 elements to reduce amplitude.
    Move like:
    3 from left
    2 from left 1 from right
    1 from left 2 from right
    3 from right
    """
    array.sort()
    right = len(array)-1
    print(array)
    ans = float("inf")
    for i in range(4):
        print(array[right-i], array[3-i])
        ans = min(ans, array[right-i]-array[3-i])


    return ans



print(solve([-1, 3, -1, 8, 5, 4]))
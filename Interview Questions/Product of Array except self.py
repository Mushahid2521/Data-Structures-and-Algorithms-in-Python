#         [1,2,3,4]
# Right: [24,12,4,1]
# Left: [1,1,2,6]
def productExceptSelf(array):
    l = len(array)
    left, right = [1]*l, [1]*l
    ans = [1]*l
    # Left Product
    temp = 1
    for i in range(1, l):
        left[i] = temp*array[i-1]
        temp = left[i]

    # Right Product
    temp = 1
    for i in range(l-2, -1, -1):
        right[i] = temp*array[i+1]
        temp = right[i]

    # Find result by finding left and right product
    for i in range(l):
        ans[i] = left[i]*right[i]

    return ans

print(productExceptSelf([1,2,3,4]))
def kadane(array):
    l = len(array)
    if l==0:
        return 0
    if l==1:
        return array[0]

    first = array[0]
    second = max(array[0], array[1])

    for i in range(2, l):
        current = max(first+array[i], second)
        first = second
        second = current

    return second

def dp(array):
    l = len(array)
    cache = [-1]*(l+1)
    if l == 0:
        return 0
    if l == 1:
        return array[0]

    if l == 2:
        return max(array[0], array[1])

    if l == 3:
        return max(array[0]+array[2], array[1])

    def f(i):
        if i >= l:
            return 0
        if cache[i]!=-1:
            return cache[i]

        cache[i] = max(array[i]+f(i+2), array[i], array[i]+f(i+3))
        return cache[i]

    f(0)
    return max(cache)

print(kadane([75, 105, 120, 75, 90, 135]))

print(dp([75, 105, 120, 75, 90, 135]))
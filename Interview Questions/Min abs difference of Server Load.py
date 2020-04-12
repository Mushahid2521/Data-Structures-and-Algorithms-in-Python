def minAbsDifference(array):
    l = len(array)
    cache = [[-1]*(sum(array)+1) for _ in range(l)]


    def dp(i, s):  # arguments are stone index and current sum
        if i == len(array):  # end of array, return the current sum (abs)
            return abs(s)

        if cache[i][s]!=-1:
            return cache[i][s]

        cache[i][s] = min(dp(i+1, s+array[i]), dp(i+1, s-array[i])) # try summing or subtracting each stone value
        return cache[i][s]

    return dp(0, 0)


print(minAbsDifference([1, 2, 3, 4, 15]))
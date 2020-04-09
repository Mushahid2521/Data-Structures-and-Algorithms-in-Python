def solve(array):
    profit = 0
    for i in range(1, len(array)):
        profit += max(array[i]-array[i-1], 0)

    return profit


print(solve([7,1,5,3,6,4]))
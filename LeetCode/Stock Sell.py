def solve(array):
    l = len(array)

    if l <=1 :
        return 0

    pre_start = 0
    start = 0
    end = 0

    max1 = 0
    buy = array[0]

    for i in range(l):
        if array[i] < buy:
            pre_start = i
            buy = array[i]

        else:
            diff = array[i] - buy
            if diff>max1:
                max1 = diff
                start = pre_start
                end = i


    if max1==0:
        return 0

    max2 = 0

    if start > 1:
        buy = array[0]

        for i in range(1, start):
            if array[i] < buy:
                buy = array[i]

            else:
                diff = array[i] - buy
                max2 = max(diff, max2)

    if l - end - 1 > 1:
        buy = array[end+1]

        for i in range(end+2, l):
            if array[i] < buy:
                buy = array[i]

            else:
                diff = array[i] - buy
                max2 = max(max2, diff)

    if end - start > 2:
        sell = array[start+1]

        for i in range(start+2, end):
            if array[i] > sell:
                sell = array[i]

            else:
                diff = sell - array[i]
                max2 = max(max2, diff)

    return max1+max2






print(solve([1,4,2]))
def LIS(array):
    l = len(array)
    cache = [None]*(l+1)
    dir = [-1]*(l+1)

    def longest(i):
        if cache[i]!=None:
            return cache[i]

        maxi = 0
        for j in range(i+1, l):
            if(array[j]> array[i]):
                if longest(j) > maxi:
                    maxi = longest(j)
                    dir[i] = j

        cache[i] = 1 + maxi
        return cache[i]

    def print_path(start):
        print(f"Path: {start}", end=" ")
        while(dir[start]!=-1):
            print(dir[start], end=" ")
            start = dir[start]

    lis = 0
    start = -1

    for i in range(l):
        if (longest(i)>lis):
            lis = longest(i)
            start = i

    print(f"Longest LIS: {lis} from staring at {start}")
    print_path(start)


LIS([5,0,9,2,7,3,7,8,9])

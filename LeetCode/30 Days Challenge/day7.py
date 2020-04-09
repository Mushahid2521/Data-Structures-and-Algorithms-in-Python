def solve(array):
    cache = [0]*(1005)
    cnt = 0
    for i, val in enumerate(array):
       cache[val] = 1

    for val in array:
        if cache[val+1]!=0:
            cnt+=1

    return cnt


print(solve(([1,3,2,3,5,0])))


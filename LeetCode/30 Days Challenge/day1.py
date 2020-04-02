def solve(array):
    array.sort()
    l = len(array)
    if l==1:
        return array[0]
    flag = 1
    val = array[0]
    for i in range(1,l):
        if array[i]==val and flag==1:
            flag = 0

        elif array[i]!=val and flag==1:
            return val

        elif flag==0:
            val = array[i]
            flag+=1

    return val


print(solve([4,1,2,1,2]))


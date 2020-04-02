def printCombination(array, n, r):

    data = [0]*r

    cobinationUtil(array, data, 0, n-1, 0, r)


def cobinationUtil(array, data, start, end, index, r):

    if(index==r):
        print(data)
        return

    i = start

    while(i<=end and end-i+1 >= r - index):
        data[index] = array[i]
        cobinationUtil(array, data, i+1, end, index+1, r)
        i+=1


if __name__=='__main__':
    arr = [1, 2, 3, 4, 5];
    r = 3;
    n = len(arr);
    printCombination(arr, n, r);

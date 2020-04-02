def search(array, p):
    dic = {key:val for val, key in enumerate(array)}
    #print(dic)

    array.sort()

    low = 0
    high = len(array)

    while(low<high):

        mid = int((low+high)/2)

        if(array[mid]==p): return dic[p]
        else:
            if(array[mid]<p):
                low = mid
            else:
                high = mid


if __name__=='__main__':
    ar = [4]
    print(search(ar, 4))
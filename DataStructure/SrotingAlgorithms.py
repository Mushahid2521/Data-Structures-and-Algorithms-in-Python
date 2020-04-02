def insertionSort(array):

    for i in range(1, len(array)):
        x = array[i]
        j = i -1

        while (j>=0 and array[j]>x):
            array[j+1] = array[j]
            j-=1

            array[j+1] = x


def selectionSort(array):

    l = len(array)
    for i in range(0, l):
        for j in range(i+1, l):
            if(array[i]>array[j]):
                x = array[j]
                array[j] = array[i]
                array[i] = x




def bubbleSort(array):

    l = len(array)
    c = 0
    for i in range(0, l):
        # If there is no swap in an iteration then break the loop means, the array is already sorted
        p = 0
        for j in range(1, l-i):
            if(array[j]<array[j-1]):
                x = array[j]
                array[j] = array[j-1]
                array[j-1] = x
                p = 1

        if(p==0): break
        c+=1

    return c



def mergeSort(lo, hi):

    if(lo==hi): return
    mid = int(lo+hi)/2

    mergeSort(lo, mid)
    mergeSort(mid+1, hi)

    i = lo; j = mid+1;

    temp = []

    for k in range(lo, hi):
        if(i==mid+1):
            temp.append(array[j])
            j+=1

        elif(j==hi+1):
            temp.append(array[i])
            i+=1

        elif(array[j]>array[i]):
            temp.append(array[i])
            i+=1

        else:
            temp.append(array[j])
            j+=1

    for i, item in enumerate(temp): array[i] = item


def countingSort(array):
    maxx = max(array)

    temp = [0 for p in range(0,maxx+1)]


    for item in array:
        #print(item)
        temp[item]+=1

    j = 0
    for i, val in enumerate(temp):
        if(temp[i]==0): continue
        else:
            for p in range(0, temp[i]):
                array[j] = i
                j+=1


if __name__ == "__main__":
    ar = int(input())
    array = list(map(int, input().split()))

    #insertionSort(arr)
    #selectionSort(arr)
    print(bubbleSort(array)-1)
    #mergeSort(0, len(array))
    #countingSort(array)
    #array.sort()
    #print(array)
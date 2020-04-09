def concat(arr1, arr2, n, m):
    # arr1 is n+m size
    l = n+m-1
    n-=1
    m-=1
    while l>=0:
        if n>=0 and m>=0:
            if arr1[n]>=arr2[m]:
                arr1[l] = arr1[n]
                n-=1

            else:
                arr1[l] = arr2[m]
                m-=1

        elif n>=0:
            arr1[l] = arr1[n]
            n-=1

        else:
            arr1[l] = arr2[m]
            m-=1

        l-=1

    return arr1


print(concat([5,9,15,20,0,0,0,0,0,0], [1,3,6,8,19,25], 4, 6))
# Return the array1 with the sorted n+m array when arr1 and arr2 are initially sorted



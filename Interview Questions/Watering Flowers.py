def watering(array, cap1, cap2):
    l = len(array)

    lo = 0
    hi = l-1


    myRes = 0
    frnRes = 0

    cnt = 0

    while lo <= hi:
        if lo==hi:
            if myRes+frnRes < array[lo]:
                myRes += cap1
                cnt+=1

        else:
            if array[lo] > myRes:
                myRes += cap1
                myRes -= array[lo]
                cnt+=1
            else:
                myRes -= array[lo]

            if array[hi] > frnRes:
                frnRes += cap2
                frnRes -= array[hi]
                cnt+=1
            else:
                myRes -= array[hi]

        lo+=1
        hi-=1

    return cnt


print(watering([2,4,5,1,2], 5, 7))



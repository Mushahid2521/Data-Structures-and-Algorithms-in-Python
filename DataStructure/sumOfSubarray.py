def ans():
    T = int(input())

    for i in range(0, T):
        l, s = (map(int, input().split()))
        arr = list(map(int, input().split()))

        sumArr = []
        sumArr.append(0)
        sum = 0
        for i, val in enumerate(arr):
            sum += val
            sumArr.append(sum)

        a = 0
        b = 1


        while (True):
            dif = sumArr[b] - sumArr[a]
            if (dif > s):
                if (b > l):
                a += 1
            elif (dif < s):
                if(b>l): a+=1
                b += 1
            else:
                break

        print("{} {}".format(a+1, b))



if __name__=='__main__':
    ans()




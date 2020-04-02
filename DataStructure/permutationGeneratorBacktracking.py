def toString(a):
    print(''.join(a))


def permute(a, l, r):
    if(l==r):
        toString(a[0:r])

    else:
        for i in range(l, r):
            a[i], a[l] = a[l], a[i]
            permute(a, l+1, r)
            a[i], a[l] = a[l], a[i]




if __name__=='__main__':
    S = "ABC"
    permute(list(S), 0, len(S))

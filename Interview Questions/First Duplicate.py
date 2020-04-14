# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q

def firstDuplicate(a):
    l = len(a)

    for i in range(l):
        if a[abs(a[i]) - 1] < 0:
            return abs(a[i])

        a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]

    return -1

print(firstDuplicate([2, 1, 3, 5, 3, 2]))
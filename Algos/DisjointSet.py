def find(x):
    if arr[x]==x:
        return x

    return find(arr[x])


def union(t,x,y):
    a = find(x)
    b = find(y)

    if t==1:
        if (a==b):
            print("Yes", end="\n")
        else:
            print("No", end="\n")

    else:
        arr[max(a,b)] = min(a,b)



if __name__=="__main__":
    N, Q = map(int, input().split())

    arr = [i for i in range(0,N+1)]

    for i in range(1,Q+1):
        t, x, y = map(int, input().split())

        union(t, x, y)



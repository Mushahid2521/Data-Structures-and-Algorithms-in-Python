def build(node, start, end):
    if (start == end):
        sum[node] = arr[start]
        return

    mid = int((start+end)/2)

    build(node*2, start, mid)
    build(node*2+1, mid+1, end)

    sum[node] = sum[node*2] + sum[node*2+1]

def update(node, start, end, pos, val):
    if (start == end):
        arr[pos]+=val
        sum[node]+= val

    else:
        mid = int((start+end)/2)
        if (pos <=mid):
            update(node*2, start, mid, pos, val)
        else:
            update(node*2+1, mid+1, end, pos, val)

        sum[node] = sum[node*2] + sum[node*2+1]


def query(node, start, end, l, r):
    if (r < start or end < l):
        return 0
    if (l <= start and end <= r):
        return sum[node]

    mid = int((start+end)/2)
    x = query(node*2, start, mid, l, r)
    y = query(node*2+1, mid+1, end, l, r)

    return x+y

if __name__=="__main__":
    arr = [i for i in range(1,9)]

    sum = [None]*(4*len(arr))


    build(1,0,len(arr)-1)



def build(node, start, end):
    if (start == end):
        sum[node] = arr[start]
        return

    mid = int((start+end)/2)

    build(node*2, start, mid)
    build(node*2+1, mid+1, end)

    sum[node] = min(sum[node*2] , sum[node*2+1])

def update(node, start, end, pos, val):
    if (start == end):
        arr[pos] = val
        sum[node] = val

    else:
        mid = int((start+end)/2)
        if (pos <=mid):
            update(node*2, start, mid, pos, val)
        else:
            update(node*2+1, mid+1, end, pos, val)

        sum[node] = min(sum[node*2] , sum[node*2+1])


def query(node, start, end, l, r):
    if (r < start or end < l):
        return 1000000
    if (l <= start and end <= r):
        return sum[node]

    mid = int((start+end)/2)
    x = query(node*2, start, mid, l, r)
    y = query(node*2+1, mid+1, end, l, r)
    return min(x,y)

if __name__=="__main__":

    N, Q = map(int, input().split())

    arr = list(map(int, input().split()))
    sum = [None]*(4*N)
    build(1, 0, N-1)
    for i in range(0,Q):

        q, l, r = input().split()

        if (q=='q'):
            print(query(1, 0, N-1, int(l)-1, int(r)-1), end='\n')
        else:
            update(1, 0, N-1, int(l)-1, int(r))

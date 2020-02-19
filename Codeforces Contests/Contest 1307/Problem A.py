t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    ar = list(map(int, input().split()))

    ans = 0
    idx = 1

    while(n>1 and idx<n and d>0):
        if(ar[idx]==0):
            idx+=1
            continue

        div = int(d/idx)
        if(div==0):
            break

        if(ar[idx]>=div):
            ans+=div
            break
        else:
            ans+=ar[idx]
            d-=(ar[idx]*idx)
            idx+=1

    print(ans+ar[0])
def solve(n, array, x):
    flag = [False]*(105)
    n = len(array)

    for i in range(n):
        flag[array[i]] = True


    for i in range(1,105):
        if flag[i]==False and x!=0:
            flag[i]=True
            x-=1

    idx = 0
    for i in range(1,105):
        if flag[i]==False:
            idx = i
            break

    idx-=1
    return idx





if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))

        print(solve(n, arr, x))

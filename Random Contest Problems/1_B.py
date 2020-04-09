def solve(N,M, array):
    sum_ = sum(array)
    array.sort()

    for i in range(N-1, N-M-1, -1):
        if array[i] < (1/(4*M))*sum_:
            return "No"

    return "Yes"


if __name__=="__main__":
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solve(N, M, arr))
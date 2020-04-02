def dp(footman, horseman, i, j):
    if(state[footman][horseman][i][j]!=-1):
        return state[footman][horseman][i][j]
    if(footman+horseman==0):
        return 1
    ret1, ret2 = 0, 0
    if(i<k1 and footman>0):
        ret1 = dp(footman-1, horseman, i+1, 0)
    if(j<k2 and horseman>0):
        ret2 = dp(footman, horseman-1, 0, j+1)

    state[footman][horseman][i][j] = int((ret1+ret2)%1e8)
    return state[footman][horseman][i][j]




if __name__=="__main__":
    n1, n2, k1, k2 = map(int, input().split())
    state = [[[[-1 for _ in range(k2+1)] for _ in range(k1+1)] for _ in range(n2+1)] for _ in range(n1+1)]
    print(dp(n1, n2, 0, 0))
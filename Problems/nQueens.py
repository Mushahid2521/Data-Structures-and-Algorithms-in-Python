def nQueens(at, n):

    if(at==n+1):
        arr = [[0]*9]*9
        for p in range(1,n+1):
            for q in range(1, n+1):
                if(queen[q]==1): arr[p][q] = 1
        return

    for i in range(1,n+1):
        if(column[i] or diagonal1[i+at] or diagonal2[n+i-at]): continue
        queen[at] = i
        column[i] = diagonal1[i+at] = diagonal2[n+i-at] = 1
        nQueens(at+1, n)
        column[i] = diagonal1[i+at] =  diagonal2[n+i-at] = 0



if __name__=='__main__':
    n = int(input())
    column = [0]*(n+2); diagonal1 = [0]*((n+2)*2); diagonal2 = [0]*((n+2)*2); queen = [0]*(n+2)

    nQueens(1,n)

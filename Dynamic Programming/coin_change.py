def dp(i, amount):
    if(i==len(coins)):
        return True if amount==make else False

    if(sum[i][amount]!=-1):
        return sum[i][amount]

    ret1, ret2 = 0, 0
    if(amount+coins[i]<=make):
        ret1 = dp(i, amount+coins[i])

    ret2 = dp(i+1, amount)

    sum[i][amount] = ret1|ret2
    return sum[i][amount]


def improved_dp(i, amount):
    if(i>=5):
        return 1 if amount==0 else 0

    if(sum[i][amount]!=-1):
        return sum[i][amount]

    ret1, ret2 = 0, 0
    if(amount-coins[i]>=0):
        ret1 = improved_dp(i, amount-coins[i])

    ret2 = improved_dp(i+1, amount)
    sum[i][amount] = ret1+ret2
    return sum[i][amount]



if __name__=="__main__":
    coins = [50,25,10,5,1]
    sum = [[-1 for _ in range(7490)] for _ in range(6)]
    while True:
        make = input()
        if(not make):
            break
        print(improved_dp(0, int(make)))

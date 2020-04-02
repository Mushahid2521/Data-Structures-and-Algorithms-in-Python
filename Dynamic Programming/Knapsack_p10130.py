def maxForOne(i, w, individual_capacity):
    if(i == N):
        return 0

    if(item_capacity[i][w]!=-1):
        return item_capacity[i][w]

    if(w+weight[i] <= individual_capacity):
        profit1 = price[i] + maxForOne(i+1, w+weight[i], individual_capacity)
    else:
        profit1 = 0

    profit2 = maxForOne(i+1, w, individual_capacity)

    item_capacity[i][w] = max(profit1, profit2)
    return item_capacity[i][w]


if __name__=="__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())

        # Storing the price and weight for all family members
        price = [-1 for _ in range(N)]
        weight = [-1 for _ in range(N)]

        # Read the price and weight
        for i in range(N):
            p, w  = map(int, input().split())
            price[i] = p
            weight[i] = w

        G = int(input())

        capacity = [-1 for _ in range(G)]

        for i in range(G):
            capacity[i] = int(input())

        total_val = 0

        for individual_capacity in sorted(capacity):
            item_capacity = [[-1 for _ in range(individual_capacity + 1)] for _ in range(N)]
            val = maxForOne(0, 0, individual_capacity)
            #print(val, individual_capacity)
            total_val+=val

        print(total_val)


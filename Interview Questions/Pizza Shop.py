def closestPrice(pizzas, toppings, x):
    new_toppings = [0]
    for i in range(len(toppings)):
        new_toppings.append(toppings[i])
        for j in range(i + 1, len(toppings)):
            new_toppings.append(toppings[i] + toppings[j])
    new_toppings.sort()

    diff = float("inf")
    val = 0
    for piz in pizzas:
        for top in new_toppings:
           if diff > abs(x-(piz+top)):
               diff = x - (piz+top)
               val = piz+top

    return round(val,3)


print(closestPrice([467, 334, 0, 169, 224, 478, 358], [564.022, 194.111, 808.932, 585.424, 480.393, 350.941, 896.066], 1000))






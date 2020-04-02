def isHappy(num):
    visited = set()

    while num!=1 and num not in visited:
        visited.add(num)
        num = sum(map(lambda x:int(x)**2, str(num)))

    return not num in visited


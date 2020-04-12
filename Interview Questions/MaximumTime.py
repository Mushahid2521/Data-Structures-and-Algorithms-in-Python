def maximumTime(string):
    h1 = string[0]
    h2 = string[1]
    m1 = string[3]
    m2 = string[4]

    if h1=='?' and h2 =='?':
        h1 = '2'
        h2 = '3'

    elif h2=='?':
        if h1=='2':
            h2 = '3'

        else:
            h2 = '9'

    elif h1=='?':
        if h2 <= '3':
            h1 = '2'
        else:
            h1 = '1'

    if m1=='?' and m2=='?':
        m1 = '5'
        m2 = '9'

    elif m1=='?':
        m1 = '5'

    elif m2=='?':
        m2 = '9'

    return h1+h2+':'+m1+m2


print(maximumTime("0?:??"))
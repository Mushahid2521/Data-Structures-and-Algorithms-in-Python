import stack


if __name__=='__main__':
    arr = [[0, 0, 0, 0, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 1, 1, 1],
           [0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]]

    #for i in range(0, len(arr)):
    #    print(arr[i])

    new_arr = arr.copy()

    for i in range(1,len(arr)):
        for j in range(0, len(arr[i])):
            new_arr[i][j]+=new_arr[i-1][j]

    for i in range(0, len(new_arr)):
        print(new_arr[i])

    max = 0
    idx = 0
    id_stack = stack.Stack()
    val_stack = stack.Stack()

    for i in range(0, len(new_arr)):
        for j in range(0, len(new_arr[i])):
            p = new_arr[i][j]
            if val_stack.isEmpty():
                val_stack.push(p)
                id_stack.push(j)

            else:
                c = val_stack.retData()
                if (p>=c):
                    val_stack.push(p)
                    id_stack.push(j)

                else:
                    while not val_stack.isEmpty():
                        c = val_stack.pop()
                        idx = id_stack.pop()
                        area = c*(j-idx)
                        if (area>max): max = area
                    val_stack.push(p)
                    id_stack.push(idx)


        val_stack = stack.Stack()
        id_stack = stack.Stack()

    print(max)
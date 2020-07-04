def solve(string, shifts):
    l = len(string)
    for shift in shifts:
        new_string = ''
        #dir, amount = shift[0], shift[1]

        # Left Shift
        if shift[0]==0:
            new_string = new_string+string[shift[1]:]+string[:shift[1]]
            string = new_string

        else:
            # print(string[:l-shift[1]], string[l-shift[1]:][::-1], string[l-shift[1]:])
            new_string = new_string+string[l-shift[1]:]+string[:l-shift[1]]
            string = new_string


    return string


print(solve("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))
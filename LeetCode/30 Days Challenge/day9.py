def solve(string1, string2):
    s1 = ''
    s1_l = len(string1)-1

    flag = 0
    for i in range(s1_l, -1, -1):
        if string1[i]!='#' and flag==0:
            s1+=string1[i]

        elif string1[i]!='#' and flag!=0:
            flag-=1

        else:
            flag+=1


    s2 = ''
    s2_l = len(string2)-1
    flag = 0
    for i in range(s2_l, -1, -1):
        if string2[i]!='#' and flag==0:
            s2+=string2[i]

        elif string2[i]!='#' and flag!=0:
            flag-=1

        else:
            flag+=1


    return s1==s2



print(solve("a##c", "#a#c#"))
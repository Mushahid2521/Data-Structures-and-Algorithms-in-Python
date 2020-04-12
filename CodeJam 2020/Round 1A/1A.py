def solve(t):
    n = int(input())

    pref, suff = "", ""
    flag = True
    ans = ""
    for i in range(n):
        s = str(input())
        l, r = 0, len(s)-1
        cur_pref, cur_suff = "", ""
        for j in range(len(s)):
            if s[j]=='*':
                break
            cur_pref+=s[j]
            l = j

        if len(cur_pref) > len(pref):
            pref, cur_pref = cur_pref, pref

        if len(cur_pref) > 0 and pref[0:len(cur_pref)] != cur_pref:
            flag = False

        for j in range(len(s)-1, -1, -1):
            if s[j]=='*':
                break
            cur_suff+=s[j]
            r = j

        cur_suff = cur_suff[::-1]
        if len(cur_suff) > len(suff):
            suff, cur_suff = cur_suff, suff

        #print(suff[len(suff)-len(cur_suff):] , cur_suff)
        if len(cur_suff) > 0 and str(suff[len(suff)-len(cur_suff):]) != str(cur_suff):
            flag = False

        for j in range(l+1, r):
            if s[j]=='*':
                continue
            ans+=s[j]

    if flag==False:
        print("Case #{}: *".format(t))

    else:
        print("Case #{}: {}".format(t, pref+ans+suff))



if __name__=="__main__":
    T = int(input())
    for t in range(1,T+1):
        solve(t)



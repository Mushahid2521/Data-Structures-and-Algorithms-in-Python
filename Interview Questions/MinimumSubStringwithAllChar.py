def minSubstringWithAllChars(s, t):
    if len(s)==0:
        return ""

    res = ""
    left = 0
    right = 0

    maxlen = float("inf")

    got_dict = {c:0 for c in t}

    def desirable():
        for val in got_dict.values():
            if val<=0:
                return False
        return True


    while right < len(s):
        if not desirable():
            if s[right] in t:
                got_dict[s[right]]+=1
            right+=1


        if desirable():
            while left < right and desirable():
                if s[left] in t:
                    got_dict[s[left]]-=1
                left+=1

            if right-(left-1) <= maxlen:
                maxlen = right-(left-1)
                res = s[left-1:right]

    return res






print(minSubstringWithAllChars("adobecodebanc","abc"))
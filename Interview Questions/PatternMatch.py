# https://app.codesignal.com/interview-practice/task/3PcnSKuRkqzp8F6BN

def areFollowingPatterns(strings, patterns):
    str_set = {}
    ptr_set = {}

    if len(strings) != len(patterns):
        return False

    l = len(strings)
    if l==1:
        return True
    if len(set(strings))!=len(set(patterns)):
        return False

    # for i in range(l):
    #     if strings[i] in str_set and patterns[i] in ptr_set:
    #         if str_set[strings[i]] == ptr_set[patterns[i]]:
    #             return True
    #
    #     str_set[strings[i]] = i
    #
    #     ptr_set[patterns[i]] = i

    return True



print(areFollowingPatterns(
strings=
["a",
 "b",
 "c"],
patterns=
["a",
 "b",
 "z"]))

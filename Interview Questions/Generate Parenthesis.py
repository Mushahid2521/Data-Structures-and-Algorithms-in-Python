def parenthesis(n):
    res = []

    def backtrack(res, left, right, braces):
        if left==0 and right==0:
            res.append(braces)
            return

        if left>0:
            backtrack(res, left-1, right, braces+'(')

        if right>left:
            backtrack(res, left, right-1, braces+')')

    backtrack(res, n, n, '')
    return res


print(parenthesis(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
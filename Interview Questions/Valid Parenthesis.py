def check(string):
    stack = []

    for c in string:
        if c=='(' or c=='{' or c=='[':
            stack.append(c)

        else:
            if not stack:
                return "not balanced"
            if c==')' and stack.pop()!='(':
                return "not balanced"

            elif c == '}' and stack.pop()!='{':
                return "not balanced"

            elif c == ']' and stack.pop()!='[':
                return "not balanced"

    return "not balanced" if stack else "balanced"


if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        s = str(input())
        print(check(s))

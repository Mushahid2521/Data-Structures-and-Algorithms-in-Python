# UnSolved. TLE


class Solve:
    def solveString(self, string):

        def check(s, start, count):
            if count < 0:
                return False

            for i in range(start, len(s)):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    if count<=0:
                        return False
                    count -= 1

                elif s[i] == '*':
                    return check(s, i + 1, count + 1) or check(s, i + 1, count) or check(s, i + 1, count - 1)

            return count==0

        return check(string, 0, 0)


class Solution:
    def checkValidString(self, s):
        ss = Solve()
        return ss.solveString(s)


s = Solution()
print(s.checkValidString("(((*)"))


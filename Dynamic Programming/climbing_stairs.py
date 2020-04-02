def dp(n, state):
    if(state[n]!=-1):
        return state[n]
    elif(n==0):
        return 1
    elif(n==1):
        return 1

    state[n] = dp(n-1, state)+dp(n-2, state)
    return state[n]

class Solution(object):
    def climbStairs(self, n):
        state = [-1 for _ in range(n+1)]
        print(dp(n, state))


s = Solution()
s.climbStairs(38)
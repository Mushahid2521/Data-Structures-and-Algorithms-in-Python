def longest_palindrome_length(string):
    N = len(string)
    cache = [[None]*N for _ in range(N)]
    left, right = 0, 0

    def find_length(i, j):
        if(cache[i][j]!=None):
            return cache[i][j]

        if(i>j):
            return 0

        if(i==j):
            return 1

        if(string[i]==string[j]):
            return find_length(i+1, j-1) + 2

        ans = max(find_length(i+1, j), find_length(i, j-1))
        cache[i][j] = ans
        return ans

    return find_length(0, N-1)

print(longest_palindrome_length("bbbab"))
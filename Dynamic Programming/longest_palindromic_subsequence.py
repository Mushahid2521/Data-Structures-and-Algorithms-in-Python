def longest_palindorme_sequence(string):
    N = len(string)
    cache = [[None]*N for _ in range(N)]

    def is_palindrome(lo, hi):
        if(cache[lo][hi]!=None):
            return cache[lo][hi]
        # There is only one character
        if lo==hi:
            return True
        # The left most and right most char is same
        elif string[lo]==string[hi]:
            return True

        ans = False if string[lo]!=string[hi] else is_palindrome(lo+1, hi-1)
        cache[lo][hi] = ans
        return ans

    def generate_palindromes():
        ret = []
        longest = N
        found = False

        if not string:
            return ['']

        for l in range(N, 0, -1):
            found = False
            for s in range(N-l+1):
                if is_palindrome(s, s+l-1):
                    found = True
                    ret.append(string[s:s+l])

            if found:
                break

        return ret

    return generate_palindromes()


print(*longest_palindorme_sequence('cbbd'))


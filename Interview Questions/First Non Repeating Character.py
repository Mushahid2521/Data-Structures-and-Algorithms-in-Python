# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC

def firstNotRepeatingCharacter(s):
    cache = {}

    for c in s:
        temp = cache.get(c, 0)
        temp += 1
        cache[c] = temp

    for key in cache.keys():
        if cache[key] == 1:
            return key

    return '_'

print(firstNotRepeatingCharacter("abacabad"))
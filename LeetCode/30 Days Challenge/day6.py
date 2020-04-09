from collections import defaultdict
def solve(strings):
    res = defaultdict(list)
    for word in strings:
        res[''.join(sorted(word))].append(word)

    return list(res.values())

print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))

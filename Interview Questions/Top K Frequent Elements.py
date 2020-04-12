from collections import defaultdict

def topKfrequent(array, k):
    counts = defaultdict(int)
    for val in array:
        counts[val]+=1

    res = []
    for key, val in counts.items():
        res.append([val, key])

    res.sort(key=lambda x: x[0], reverse=True)

    ans = []
    for i in range(k):
        ans.append(res[i][1])

    return ans





print(topKfrequent([1,1,1,2,2,3], 2))
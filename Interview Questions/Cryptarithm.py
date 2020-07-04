# https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H

def isCryptSolution(crypt, solution):
    mapping = {}
    for pair in solution:
        mapping[pair[0]] = int(pair[1])


    def to_int(word):
        l = len(word)
        val = 0
        for idx, char in enumerate(reversed(word)):
            val += (10 ** idx) * mapping[char]

        if l!=len(str(val)):
            return False
        return val+1

    if to_int(crypt[2]) and to_int(crypt[0]) and to_int(crypt[1]):
        return to_int(crypt[2])+1==to_int(crypt[0])+to_int(crypt[1])


print(isCryptSolution(
["A",
 "A",
 "A"],
[["A","0"],
 ]))


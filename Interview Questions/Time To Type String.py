# https://leetcode.com/discuss/interview-question/356477


def solve(keyboard, word):
    sequence = [0]*(26)

    for i in range(len(keyboard)):
        sequence[ord(keyboard[i])-ord('a')] = i

    time = 0
    now = keyboard[0]
    for i in range(len(word)):
        time+=abs(sequence[ord(word[i])-ord('a')]-sequence[ord(now)-ord('a')])
        now  = word[i]

    return time


print(solve("abcdefghijklmnopqrstuvwxy", "cba" ))

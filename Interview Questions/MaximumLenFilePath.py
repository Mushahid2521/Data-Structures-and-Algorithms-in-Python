# https://app.codesignal.com/interview-practice/task/iXJRYae6TBqc4ymFg

## Todo: Not Understood


def longestPath(fileSystem):
    maxlen = 0
    pathlen = {0:0}
    for line in fileSystem.splitlines():
        name = line.lstrip('\t')
        depth = len(line)-len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth]+len(name))
        else:
            pathlen[depth+1] = pathlen[depth] + len(name)+1
    return maxlen


print(longestPath("user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt"))
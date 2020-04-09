if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        s = str(input())
        l = len(s)

        words = []
        res = ''
        for i in range(l):
            if s[i]=='.':
                words.append(res)
                res = ''
            else:
                res+=s[i]

        words.append(res)
        l = len(words)

        res = ''
        for i in range(l-1,-1,-1):
            res+=words[i]
            res+='.'

        print(res[:-1])


#i.like.this.program.very.much
#much.very.program.this.like.i
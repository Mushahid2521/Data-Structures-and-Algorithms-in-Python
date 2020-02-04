while True:
    inp = input()
    if not inp:
        break
    a,b = map(str, inp.split())
    a1, a2 = ord(a[0]) - ord('a'), ord(a[1]) - ord('1')
    b1, b2 = ord(b[0]) - ord('a'), ord(b[1]) - ord('1')

    directions = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
    vis, queue, level = [[False for _ in range(8)] for _ in range(8)], [], [[0 for _ in range(8)] for _ in range(8)]
    vis[a1][a2] = True
    queue.append([a1,a2])
    level[a1][a2] = 0

    while queue:
        l = queue.pop(0)
        for d in directions:
            tx = l[0] + d[0]
            ty = l[1] + d[1]
            if(tx>=0 and tx<8 and ty>=0 and ty<8 and vis[tx][ty]==False):
                level[tx][ty] = level[l[0]][l[1]] + 1
                vis[tx][ty] = True
                queue.append([tx,ty])

    print(f'To get from {a} to {b} takes {level[b1][b2]} knight moves.')



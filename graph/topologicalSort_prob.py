t = 0
while True:
    n = input()
    if(not n):
        break

    t+=1
    n = int(n)

    graph = {}
    inDegree = {}
    visited = {}

    for _ in range(n):
        s = str(input())
        graph[s] = []
        inDegree[s] = 0
        visited[s] = False

    m = int(input())
    for _ in range(m):
        s1, s2 = map(str, input().split())
        graph[s1].append(s2)
        inDegree[s2]+=1

    queue = []
    order = []
    for key in inDegree.keys():
        if(inDegree[key]==0):
            queue.append(key)
            visited[key] = True

    while queue:
        now = queue.pop(0)
        order.append(now)
        for itm in graph[now]:
            if(visited[itm]==False):
                inDegree[itm]-=1
                if(inDegree[itm]==0):
                    visited[itm] = True
                    queue.append(itm)

    print(f"Case #{t}: Dilbert should drink beverages in this order:", *order)



